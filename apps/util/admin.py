from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from imagekit.admin import AdminThumbnail

from apps.core.admin import admin_general, ControlsAdminMixin
from . import models


class CargoInline(GenericTabularInline):
    model = models.Cargo
    extra = 1
    suit_classes = 'suit-tab suit-tab-cargo'


class HorarioInline(GenericTabularInline):
    model = models.Horario
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


class RedSocialInline(GenericTabularInline):
    model = models.RedSocial
    extra = 1
    suit_classes = 'suit-tab suit-tab-netphone'


class TelefonoInline(GenericTabularInline):
    model = models.Telefono
    extra = 1
    suit_classes = 'suit-tab suit-tab-netphone'


class EmailInline(GenericTabularInline):
    model = models.Email
    extra = 1
    suit_classes = 'suit-tab suit-tab-netphone'


class ImagenInline(GenericTabularInline):
    model = models.Imagen
    extra = 1
    suit_classes = 'suit-tab suit-tab-imagen'


@admin.register(models.Localidad, site=admin_general)
class LocalidadAdmin(ControlsAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'departamento')
    search_fields = ('nombre', 'departamento__nombre')
    list_filter = ('departamento',)


@admin.register(models.Departamento, site=admin_general)
class DepartamentoAdmin(ControlsAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'provincia')
    search_fields = ('nombre', 'provincia__nombre')


admin_general.register(models.Pais)
admin_general.register(models.Provincia)
admin_general.register(models.Autoridad)
admin_general.register(models.Cargo)
admin_general.register(models.Horario)
admin_general.register(models.RedSocial)
admin_general.register(models.Telefono)
admin_general.register(models.Email)
admin_general.register(models.Imagen)
