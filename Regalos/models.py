from django.db import models

class Regalos(models.Model):
    idInvitados = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Nombre = models.CharField(max_length=50)
    ImagenUrl = models.URLField(blank = True, null=True, max_length=1000, verbose_name='Url Imagen del Regalo' )
    EnlaceRegalo = models.URLField(blank=True, null=True, max_length=1000, verbose_name='Enlace del Regalo')


    
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name_plural = "Regalos"
