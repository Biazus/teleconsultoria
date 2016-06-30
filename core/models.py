from django.db import models

# Create your models here.
class Requester(models.Model):
    requester_id = models.AutoField(primary_key=True)
    requester_name = models.CharField(max_length=45, verbose_name='Nome')
    requester_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    requester_phone = models.CharField(max_length=18, blank=True, verbose_name='Telefone')
    #requester_favorito = models.BooleanField(verbose_name='CPF')
    
    def get_absolute_url(self):
       return reverse('requester_update', args=[str(self.id)])
    
    def __unicode__(self):
        return self.requester_name
    class Meta:
        db_table = u'requester'
        verbose_name = 'Requester'
        verbose_name_plural = 'Requesters'
        ordering = ['requester_name']
