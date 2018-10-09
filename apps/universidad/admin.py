from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.util import admin as tabular
from apps.core.admin import (
    admin_general,
    ControlsAdminMixin,
    PublicadoAdmin,
    MapAdmin
)

from . import models, forms


@admin.register(models.Universidad, site=admin_general)
class UniversidadAdmin(ControlsAdminMixin, MapAdmin, admin.ModelAdmin):
    #form = forms.UniversidadForm
    list_display = ('nombre', 'sigla',)
    list_filter = ('nombre', 'provincia',)
    search_fields = ('nombre', 'sigla')

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
                'nombre', 'descripcion', 'sigla', 
                'pagina',
            ]
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-cargo',),
            'description': 'Cargos de la universidad',
            'fields': []
        }),
        
        ('Datos', {
            'classes': ('suit-tab suit-tab-ubicacion',),
            'description': 'Ubicación de la universidad',
            'fields': [
                'nombre_direccion', 'numero_direccion', 'provincia',
                'departamento', 'localidad', 'extra', 'ubicacion'
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


@admin.register(models.Aula, site=admin_general)
class AulaAdmin(ControlsAdminMixin, MapAdmin, admin.ModelAdmin):
    pass
    