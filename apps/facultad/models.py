from datetime import date

from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as models_gis
from django.contrib.contenttypes.fields import GenericRelation

from django_autoslugfield import AutoSlugField
from tinymce.models import HTMLField

from apps.core.models import Activo
from apps.util.models import AbstractDireccion, AbstractPersona


class Facultad(AbstractDireccion, models.Model):
    class Meta:
        verbose_name_plural = 'Facultades'
        
    nombre = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    descripcion = HTMLField(null=True, blank=True)
    sigla = models.CharField(max_length=50, null=True, blank=True)
    siu = models.URLField(null=True, blank=True, help_text='URL Siu')
    aula_virtual = models.URLField(null=True, blank=True, help_text='URL Aula Virtual')
    ubicacion = models_gis.PointField()

    universidad = models.ForeignKey(
        'universidad.Universidad', 
        related_name="facultades", on_delete=models.CASCADE)
    
    cargos = GenericRelation('util.Cargo')
    horarios = GenericRelation('util.Horario')
    imagenes = GenericRelation('util.Imagen')
    emails = GenericRelation('util.Email')
    telefonos = GenericRelation('util.Telefono')
    redes_sociales = GenericRelation('util.RedSocial')

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.universidad)


class DepartamentoFacultad(AbstractDireccion, models.Model):
    class Meta:
        verbose_name = 'Departamento Facultad'
        verbose_name_plural = 'Departamentos Facultad'

    nombre = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    ubicacion = models_gis.PointField()
    
    facultad = models.ForeignKey(
        Facultad, 
        related_name='departamentos', on_delete=models.CASCADE
    )
    cargos = GenericRelation('util.Cargo')
    horarios = GenericRelation('util.Horario')
    emails = GenericRelation('util.Email')
    telefonos = GenericRelation('util.Telefono')
    redes_sociales = GenericRelation('util.RedSocial')
    
    def __str__(self):
        return '{}'.format(self.nombre)


class Carrera(models.Model):
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    DURACION = (
        ('1.0', '1 año'),
        ('1.5', '1 año y medio'),
        ('2.0', '2 años'),
        ('2.5', '2 años y medio'),
        ('3.0', '3 años'),
        ('3.5', '3 años y medio'),
        ('4.0', '4 años'),
        ('4.5', '4 años y medio'),
        ('5.0', '5 años'),
        ('5.5', '5 años y medio'),
        ('6.0', '6 años'),
        ('6.5', '6 años y medio'),
        ('7.0', '7 años'),
    )

    TIPO = (
        ('AD', 'A Distancia'),
        ('CC', 'Ciclo Complementación Curricular'),
        ('CL', 'Ciclo Licenciatura'),        
        ('GR', 'Grado'),
        ('PD', 'Post Grado'),
        ('PG', 'Pre Grado'),
    )

    nombre = models.CharField(max_length=150, null=True, blank=True)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    duracion = models.CharField(max_length=3, choices=DURACION, null=True, blank=True)
    tipo = models.CharField(max_length=2, choices=TIPO, null=True, blank=True)
    trabajo_final = models.BooleanField(default=False)
    descripcion = models.TextField(null=True, blank=True)

    departamento = models.ForeignKey(
        DepartamentoFacultad, 
        on_delete=models.CASCADE, related_name='carreras')

    def __str__(self):
        return '{}'.format(self.nombre)


class PlanEstudio(models.Model):
    class Meta:
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudio'
        unique_together = ('año', 'carrera',)
    ANO = (
        list(reversed([(str(i), str(i)) for i in range(1990, timezone.now().year + 2)]))
    )

    año = models.CharField(choices=ANO, max_length=4, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.carrera, self.año)


class Profesor(AbstractPersona, Activo):
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.nombre_apellido)