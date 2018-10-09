from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from multiselectfield import MultiSelectField
from django_autoslugfield import AutoSlugField

    
class Materia(models.Model):
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
    
    AÑO = (
        ('1', '1°'),
        ('2', '2°'),
        ('3', '3°'),
        ('4', '4°'),
        ('5', '5°'),
        ('6', '6°'),
        ('7', '7°'),
    )

    PERIODO = (
        ('AN', 'Anual'),
        ('1C', 'Primer Cuatrimetre'),
        ('2C', 'Segundo Cuatrimestre'),
    )

    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(max_length=255, unique=True, null=True, blank=True)
    año = models.CharField(max_length=1, choices=AÑO, null=True, blank=True)
    periodo = models.CharField(max_length=2, choices=PERIODO, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    sigla = models.CharField(max_length=50, null=True, blank=True)
    
    correlativas_cursar = models.ManyToManyField('self', blank=True)
    correlativas_aprobar = models.ManyToManyField('self', blank=True)
    planes_estudio = models.ManyToManyField('facultad.PlanEstudio')
    
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.nombre)


class HorarioMateria(models.Model):
    class Meta:
        verbose_name = 'Horario Materia'
        verbose_name_plural = 'Horarios de Materia'

    DIAS = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo'),

    )

    inicio = models.TimeField(null=True, blank=True)
    fin = models.TimeField(null=True, blank=True)
    dias = MultiSelectField(choices=DIAS, max_length=200, null=True, blank=True)
    
    aula = models.ForeignKey('universidad.Aula', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='horarios')

    def __str__(self):
        return '{}- {}'.format(self.materia, self.get_dias_display())


class ModoProfesor(models.Model):
    class Meta:
        verbose_name = 'Materia Profesor'
        verbose_name_plural = 'Materias Profesores'
    
    MODOS = (
        ('TE', 'Teórico'),
        ('PR', 'Práctico'),
    )

    modo = models.CharField(choices=MODOS, max_length=2)
    profesores = models.ManyToManyField('facultad.Profesor')
    horario_materia = models.OneToOneField(
        HorarioMateria, 
        on_delete=models.CASCADE,
        related_name='modo_profesores'
    )

    def __str__(self):
        return '{} - {}'.format(self.horario_materia.materia, self.get_modo_display())