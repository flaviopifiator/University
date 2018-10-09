from django.contrib import admin

from apps.util import admin as tabular
from apps.core.admin import (
    admin_general,
    ControlsAdminMixin,
    PublicadoAdmin
)

from . import models


class HorarioMateriaInline(admin.TabularInline):
    model = models.HorarioMateria
    extra = 1
    suit_classes = 'suit-tab suit-tab-horario'


@admin.register(models.Materia, site=admin_general)
class MateriaAdmin(ControlsAdminMixin, admin.ModelAdmin):
    list_display = ('nombre', 'sigla', 'codigo')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'codigo')
    filter_horizontal = ('planes_estudio', 'correlativas_cursar', 'correlativas_aprobar',)
    inlines = (
        HorarioMateriaInline,
    )

    fieldsets = [
        ('Datos', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [
                'codigo', 'nombre', 'año', 'periodo',
                'descripcion', 'sigla',
                'correlativas_cursar', 'correlativas_aprobar',
                'planes_estudio',
            ]
        }),

        ('Datos', {
            'classes': ('suit-tab suit-tab-horario',),
            'description': 'Horarios de la materia',
            'fields': []
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('horario', 'Horarios'),
    )


@admin.register(models.HorarioMateria, site=admin_general)
class HorarioMateriaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ModoProfesor, site=admin_general)
class ModoProfesorAdmin(admin.ModelAdmin):
    pass