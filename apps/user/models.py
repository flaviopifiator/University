from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.facultad.models import Facultad


class User(AbstractUser):

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('username', 'last_name', 'first_name')
    TIPO = (
        ('ES', 'Estudiante'),
        ('PE', 'Personal'),
    )

    tipo = models.CharField(choices=TIPO, max_length=2, default=TIPO[0][0])
    facultad = models.ForeignKey(
        Facultad, related_name="usuarios", 
        null=True, blank=True, on_delete=models.PROTECT
    )

    USERNAME_FIELD = 'username'

    