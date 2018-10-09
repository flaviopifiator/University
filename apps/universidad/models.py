from django.db import models
from django.contrib.gis.db import models as models_gis
from django.contrib.contenttypes.fields import GenericRelation

from django_autoslugfield import AutoSlugField

from apps.util.models import AbstractDireccion
from apps.facultad.models import Facultad


class Universidad(AbstractDireccion, models.Model):
    class Meta:
        ordering = ('nombre', 'sigla')
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        unique_together = ('nombre', 'sigla')
    
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    sigla = models.CharField(max_length=50, null=True, blank=True)
    pagina = models.URLField(null=True, blank=True, help_text='URL página web')
    ubicacion = models_gis.PointField()

    cargos = GenericRelation('util.Cargo')
    horarios = GenericRelation('util.Horario')
    imagenes = GenericRelation('util.Imagen')
    emails = GenericRelation('util.Email')
    telefonos = GenericRelation('util.Telefono')
    redes_sociales = GenericRelation('util.RedSocial')

    def __str__(self):
        if self.sigla:
            return '{} - {}'.format(self.sigla, self.nombre)
        return self.nombre


class Aula(models.Model):
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
    
    nombre = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(max_length=255, null=True, blank=True, unique=True)
    descripcion = models.TextField()
    ubicacion = models_gis.PointField()
    universidad = models.ForeignKey(Universidad, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
