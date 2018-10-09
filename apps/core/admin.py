from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from leaflet.admin import LeafletGeoAdmin

from . import filters


User = get_user_model()


class CustomAdmin(admin.AdminSite):
    site_header = site_title = 'Universidad'
    index_title = 'Administración'


admin_general = CustomAdmin(name='admin_general')


# Usar solo para aquellos modelos en donde tengan el campo universidad ForeignKey
class UniversidadUserMixin(object):
    def get_list_filter(self, request):
        list_filter = list(super().get_list_filter(request))
        if request.user.is_superuser:
            list_filter += ['universidad']
        return list_filter

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        if request.user.is_superuser:
            list_display += ['universidad']
        return list_display

    def get_queryset(self, request):
        if request.user.is_superuser is False:
            return super().get_queryset(request).filter(
                universidad=request.user.universidad
            )
        else: 
            return super().get_queryset(request)

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser == False:
            obj.universidad = request.user.universidad
            obj.save()
        else:
            return super().save_model(request, obj, form, change)
        
        
# ModelAdmin para Publicado -> Modelo Abstracto.
class PublicadoAdmin(admin.ModelAdmin):
    actions = ['publicar', 'despublicar']

    def publicar(self, request, queryset):
        # TODO: How to use LogEntry here!
        rows_update = queryset.update(publicado=timezone.now())
        message = "%s " % rows_update
        self.message_user(request, "%s registro/s publicado/s." % message)

    publicar.short_description = 'Publicar registros seleccionados'

    def despublicar(self, request, queryset):
        # TODO: How to use LogEntry here!
        rows_update = queryset.update(publicado=None)
        message = "%s " % rows_update
        self.message_user(request, "%s registro/s despublicado/s." % message)

    despublicar.short_description = 'Despublicar registros seleccionados'

    def get_actions(self, request):
        actions = super().get_actions(request)
        # TODO:
        # If user haven't permission or not member in group "publicar"
        # delete publicar and despublicar of actions.
        # del actions['publicar'] ...
        return actions

    def get_list_filter(self, request):
        list_filter = [
            filters.PublicadoListFilter
        ] + list(super().get_list_filter(request))

        return list_filter

    def get_list_display(self, request):
        return list(super().get_list_display(request)) + ['publicado']


class ControlsAdminMixin(object):
    list_controls_template = None
    list_display_links = None

    def get_controls(self, instance):
        if not self.list_controls_template:
            self.list_controls_template = 'core/generic-list-controls.html'

        return render_to_string(self.list_controls_template, {
            'instance': instance,
            'has_change_permission': self.has_change_permission(self.request),
            'has_delete_permission': self.has_delete_permission(self.request)
        })

    get_controls.short_description = ''

    def get_list_display(self, request):
        list_display = [
            'get_controls'
        ] + list(super().get_list_display(request))

        return list_display

    def get_queryset(self, request):
        self.request = request          # Use in template list_controsl_template
        return super().get_queryset(request)


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that prevents modifications through the admin.
    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    Source: https://gist.github.com/aaugustin/1388243
    """
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return (request.method in ['GET', 'HEAD'] and
                super().has_change_permission(request, obj))

    def has_delete_permission(self, request, obj=None):
        return False


class MapAdmin(LeafletGeoAdmin):
    pass