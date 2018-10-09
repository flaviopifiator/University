from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from multiselectfield import MultiSelectField

from .utils import upload_to


class Pais(models.Model):
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
        ordering = ('nombre', )
        unique_together = ('nombre',)

    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ('nombre', )
        unique_together = ("nombre", "pais")

    nombre = models.CharField(max_length=150, unique=True)
    pais = models.ForeignKey('util.Pais', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('nombre', )
        unique_together = ("nombre", "provincia")

    nombre = models.CharField(max_length=100, unique=True)
    provincia = models.ForeignKey('util.Provincia', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nombre


class Localidad(models.Model):
    class Meta:
        ordering = ('nombre', )
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        unique_together = ("nombre", "departamento")

    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey('util.Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class AbstractDireccion(models.Model):
    class Meta:
        abstract = True

    nombre_direccion = models.CharField('Nombre de Calle', max_length=100, null=True, blank=True, )
    numero_direccion = models.PositiveIntegerField('Número de Calle', null=True, blank=True)
    extra = models.CharField(max_length=400, null=True, blank=True)

    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre_direccion, self.numero_direccion)


class AbstractPersona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField('Nombre', max_length=100, null=True, blank=True)
    apellido = models.CharField('Apellido', max_length=100, null=True, blank=True)

    emails = GenericRelation('util.Email')
    telefonos = GenericRelation('util.Telefono')
    
    @property
    def nombre_apellido(self):
        return u'%s, %s' % (self.nombre, self.apellido)


class Autoridad(AbstractPersona, models.Model):
    class Meta:
        verbose_name = 'Autoridad'
        verbose_name = 'Autoridades'

    titulo = models.CharField(max_length=50, null=True, blank=True)

    @property
    def titulo_nombre(self):
        if self.titulo == None:
            self.titulo = ''

        return u'%s %s' % (self.titulo, self.nombre_apellido)
    
    def __str__(self):
        return "%s" % (self.titulo_nombre)


# Generics Models

class Cargo(models.Model):
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    nombre = models.CharField(max_length=200)
    prioridad = models.PositiveIntegerField(null=True, blank=True)

    autoridades = models.ManyToManyField(Autoridad)

    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('departamentofacultad', 'facultad', 'universidad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "(%s) %s" % (self.nombre, self.content_object)


class Horario(models.Model):
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
    
    TURNO = (
        ('TM', 'Turno Mañana'),
        ('TT', 'Turno Tarde'),
        ('TN', 'Turno Noche'),
    )

    DIAS = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo'),

    )

    turno = models.CharField(max_length=2, choices=TURNO, null=True, blank=True)
    inicio = models.TimeField(null=True, blank=True)
    fin = models.TimeField(null=True, blank=True)

    dias = MultiSelectField(choices=DIAS, max_length=14, null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('universidad', 'facultad', 'departamentofacultad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "(%s) %s" % (self.get_turno_display(), self.content_object)


class RedSocial(models.Model):
    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    FACEBOOK = 'fb'
    TWITTER = 'tw'
    INSTAGRAM = 'in'
    YOUTUBE = 'yt'

    RED = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'Youtube'),
    )

    red = models.CharField(max_length=2, choices=RED)
    url = models.URLField()
    
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('universidad', 'facultad', 'departamentofacultad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "(%s) %s" % (self.get_red_display(), self.content_object)


class Telefono(models.Model):
    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'

    FAX = 'fax'
    TELEFONO = 'tel'
    CELULAR = 'cel'

    TIPO = (
        (FAX, 'Fax'),
        (TELEFONO, 'Teléfono'),
        (CELULAR, 'Celular'),
    )

    tipo = models.CharField(max_length=3, choices=TIPO)
    numero = models.CharField(max_length=40)
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('universidad', 'facultad', 'departamentofacultad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "(%s) %s" % (self.get_tipo_display(), self.numero)


class Email(models.Model):
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
    
    email = models.EmailField(blank=True, null=True)
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('universidad', 'facultad', 'departamentofacultad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return "%s: $%s" % (self.content_object, self.email)


class Imagen(models.Model):
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

    imagen = models.ImageField(max_length=300, upload_to=upload_to)
    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )

    nombre = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    ancho = models.PositiveIntegerField(null=True, blank=True)
    largo = models.PositiveIntegerField(null=True, blank=True)
    portada = models.BooleanField(default=False)
    
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={
            'model__in': ('universidad', 'facultad')
        },
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        tag = '<img src="%s" width="100" height="50" />' % self.imagen_thumbnail.url
        return mark_safe(tag)
