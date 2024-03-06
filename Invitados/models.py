from django.db import models

class Invitados(models.Model):
    idInvitados = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    NombreCompleto = models.CharField(max_length=50)
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('cancelado', 'Cancelado'),
        ('confirmado', 'Confirmado'),
    ]
    Asistencia = models.CharField(choices=ESTADOS, default='pendiente', max_length=12)
    Mesa = models.IntegerField(blank=True, null=True, default=None)
    Cancion = models.CharField(max_length=80, blank=True)
    PROTEINAS = [
        ('cerdo', 'Cerdo'),
        ('pollo', 'Pollo'),
        ('res', 'Res'),
        ('pescado', 'Pescado'),
    ]
    Proteina = models.CharField(choices=PROTEINAS, default=False, max_length=10, blank=True)
    RESTRICCIONES = [
        ('mariscos', 'Soy alergico a los mariscos'),
        ('vegano', 'Soy vegano'),
        ('vegetariano', 'Soy vegetariano'),
        ('lacteos', 'Soy intolerante a los lacteos'),
        ('diabetico', 'Soy diabetico'),
        ('ninguna', 'Ninguna de las anteriores'),
    ]
    Restriccion = models.CharField(choices=RESTRICCIONES,default=False, max_length=30, blank=True)
    Observaciones = models.CharField(max_length=100, default=False, blank=True)
    
    
    def __str__(self):
        return self.NombreCompleto

    class Meta:
        verbose_name_plural = "Invitados"
