from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Requester(models.Model):
    requester_id = models.AutoField(primary_key=True)
    requester_name = models.CharField(max_length=45, verbose_name='Nome')
    requester_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Número de telefone deve ter o formato: '+999999999' ou: '999999999' (min: 9 e max: 15 caracteres).")
    requester_phone = models.CharField(max_length=20, validators=[phone_regex], blank=True, verbose_name='Telefone')
    requester_CPF = models.IntegerField(max_length=11, verbose_name='CPF', unique=True)
    requester_last_request_date = models.DateTimeField(default=timezone.now()- timedelta(days=1), blank=True)

    def get_absolute_url(self):
       return reverse('requester_update', args=[str(self.id)])
    
    def __unicode__(self):
        return self.requester_name
    
    def __str__(self):
        return self.requester_name
    
    class Meta:
        db_table = u'requester'
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        ordering = ['requester_name']

class Consultant(models.Model):
    consultant_id = models.AutoField(primary_key=True)
    consultant_name = models.CharField(max_length=45, verbose_name='Nome')
    consultant_CRM = models.CharField(max_length=45, verbose_name='CRM')
    consultant_graduation_date = models.DateField(default=timezone.now(), verbose_name="Data de formatura")

    def get_absolute_url(self):
       return reverse('consultant_update', args=[str(self.id)])
    
    def __unicode__(self):
        return self.consultant_name
    class Meta:
        db_table = u'consultant'
        verbose_name = 'Teleconsultor'
        verbose_name_plural = 'Teleconsultores'
        ordering = ['consultant_name']

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_description = models.TextField(max_length=500, verbose_name="Descrição", )
    requester = models.ForeignKey('Requester',on_delete=models.CASCADE, verbose_name="Solicitante", )
    tags = models.ManyToManyField("Tag", blank=True)
    
    def clean(self):
        try:
            has_requester = (self.requester is not None)
            # "self.request_id is None" ensures that it will only happen during the object creation
            if (timezone.now().date() - self.requester.requester_last_request_date.date()).days == 0 and self.request_id is None:
                raise ValidationError(('Este solicitante já criou uma solicitação hoje.'))            
        except Requester.DoesNotExist:
            #it will be handled by the validators
            pass
            
    def get_absolute_url(self):
       return reverse('request_update', args=[str(self.id)])
       
    def __unicode__(self):
        return self.request_id
        
    class Meta:
        db_table = u'request'
        verbose_name = u'Solicitação'
        verbose_name_plural = u'Solicitações'
        ordering = ['request_id']

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, )
    tag_name = models.CharField(max_length=45, unique=True, verbose_name='Nome da Tag')
    requests = models.ManyToManyField("Request", blank=True)
    
    def get_absolute_url(self):
       return reverse('tag_update', args=[str(self.id)])
       
    def __unicode__(self):
        return self.tag_name
        
    def __str__(self):
        return self.tag_name
        
    class Meta:
        db_table = u'tag'
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'
        ordering = ['tag_name']



''' Signals: From Django official doc:
    
    Django includes a “signal dispatcher” which helps allow decoupled applications 
    get notified when actions occur elsewhere in the framework. 
    In a nutshell, signals allow certain senders to notify a set of receivers 
    that some action has taken place. 
    
    You can put signal handling and registration code anywhere you like. 
    However, you’ll need to make sure that the module it’s in gets imported early on
    so that the signal handling gets registered before any signals need to be sent. 
    This makes your app’s models.py a good place to put registration of signal handlers.
'''

"""
    This function updates the last requester date of the requester to make sure that
    he won't create any other solicitation until the end of the day
"""
@receiver(post_save, sender=Request)
def update_last_request_day(sender, instance, **kwargs):
    requester = Requester.objects.get(
        requester_id=instance.requester.requester_id,
    )
    requester.requester_last_request_date = datetime.today()
    requester.save()
