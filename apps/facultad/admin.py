from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.util import admin as tabular
from apps.core.admin import (
    admin_general,
    ControlsAdminMixin,
    PublicadoAdmin,
    MapAdmin,
)

from . import models, forms


@admin.register(models.Facultad, site=admin_general)
class FacultadAdmin(ControlsAdminMixin, MapAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'sigla', 'universidad',)
    list_filter = ('nombre', 'provincia',)
    search_fields = ('nombre',)

    inlines = (
        tabular.CargoInline,
        tabular.HorarioInline,
        tabular.TelefonoInline,
        tabular.EmailInline,
        tabular.RedSocialInline,
        tabular.ImagenInline
    )

    fieldsets = [
        ('Datos', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [
                'universidad', 'nombre', 'descripcion',
                'sigla', 'siu', 'aula_virtual',
            ]
        }),
        
        ('Datos', {
            'classes': ('suit-tab suit-tab-cargo',),
            'description': 'Cargos de la facultad',
            'fields': []
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-ubicacion',),
            'description': 'Ubicación de la facultad',
            'fields': [
                'nombre_direccion', 'numero_direccion', 'extra',
                'provincia', 'departamento', 'localidad', 'ubicacion'
            ]
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-netphone',),
            'description': 'Contactos electrónicos',
            'fields': []
        }),
        
        (None, {
            'classes': ('suit-tab suit-tab-imagen',),
            'description': 'Galería de imagenes',
            'fields': []
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('cargo', 'Cargos'),
        ('ubicacion', 'Ubicación'),
        ('netphone', 'Teléfonos/ Redes Sociales'),
        ('imagen', 'Galería')
    )


@admin.register(models.DepartamentoFacultad, site=admin_general)
class DepartamentoFacultadAdmin(ControlsAdminMixin, MapAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'facultad',)
    list_filter = ('facultad',)
    search_fields = ('nombre',)

    inlines = (
        tabular.CargoInline,
        tabular.HorarioInline,
        tabular.TelefonoInline,
        tabular.EmailInline,
        tabular.RedSocialInline,
    )

    fieldsets = [
        ('Datos', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [
                'facultad', 'nombre',
            ]
        }),
        
        ('Datos', {
            'classes': ('suit-tab suit-tab-cargo',),
            'description': 'Cargos del departamento',
            'fields': []
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-ubicacion',),
            'description': 'Ubicación de la facultad',
            'fields': [
                'nombre_direccion', 'numero_direccion', 'extra',
                'provincia', 'departamento', 'localidad', 'ubicacion'
            ]
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-netphone',),
            'description': 'Contactos electrónicos',
            'fields': []
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('cargo', 'Cargos'),
        ('ubicacion', 'Ubicación'),
        ('netphone', 'Teléfonos/ Redes Sociales'),
    )


@admin.register(models.Profesor, site=admin_general)
class ProfesorAdmin(ControlsAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'apellido',)

    inlines = (
        tabular.TelefonoInline,
        tabular.EmailInline,
    )

    fieldsets = [
        ('Datos', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [
                'nombre', 'apellido', 'activo',
            ]
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-netphone',),
            'description': 'Contactos electrónicos',
            'fields': []
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('netphone', 'Teléfonos/ Emails'),
    )


admin_general.register(models.Carrera)
admin_general.register(models.PlanEstudio)