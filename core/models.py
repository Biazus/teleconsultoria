from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Requester(models.Model):
    requester_id = models.AutoField(primary_key=True)
    requester_name = models.CharField(max_length=45, verbose_name='Nome')
    requester_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    #requester_phone = models.CharField(max_length=18, blank=True, verbose_name='Telefone')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Número de telefone deve ter o formato: '+999999999' ou: '999999999' (min: 9 e max: 15 caracteres).")
    requester_phone = models.CharField(max_length=20, validators=[phone_regex], blank=True, verbose_name='Telefone')
    
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
    request_description = models.TextField(max_length=500, verbose_name="Descrição da Solicitação", )
    requester = models.ForeignKey('Requester',on_delete=models.CASCADE, verbose_name="Solicitante", )
    tags = models.ManyToManyField("Tag")
    
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
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=45, verbose_name='Nome da Tag')
    requests = models.ManyToManyField("Request")
    
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
        ordering = ['tag_id']
