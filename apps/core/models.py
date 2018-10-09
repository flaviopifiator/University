from django.db import models
from django.utils import timezone


class ActivoManager(models.Manager):
    """Retorna todos los registros que fueron publicados """

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.exclude(activo=False)


class Activo(models.Model):
    """
    Description:
    Modelo Abstracto, se utiliza para añadir el campo publicado a
    modelo, además de los métodos necesarios para dicha acción.
    """
    class Meta:
        abstract = True

    activo = models.BooleanField(default=True)

    objects = models.Manager()
    activos = ActivoManager()

    def activar(self, status=True):
        """
        status: True -> Activado
        status: False -> Inactivo.
        """

        self.activo = True if status else False
        self.save()