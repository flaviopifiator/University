from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from apps.core.admin import CustomAdmin, UniversidadUserMixin

from .models import User

admin_user = CustomAdmin(name='admin_user')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UserEditAdmin(UniversidadUserMixin, UserAdmin):
    form = MyUserChangeForm

    def get_list_display(self, request):
        list_display = ['username', 'email', 'first_name', 'last_name']
        if request.user.is_superuser:
            list_display += ['is_staff', 'is_superuser', 'is_active', 'tipo', 'facultad']
        return list_display

    def get_list_filter(self, request):
        list_filter = []
        if request.user.is_superuser:
            list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'facultad')
        return list_filter

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        fieldsets = (
            (None, {'fields': ('username', 'password')}),
            (('Información Personal'), {'fields': ('first_name', 'last_name', 'email')}),
        )
        if request.user.is_superuser:
            return (('Datos usuario', {'fields': ('tipo', 'facultad',)}),) + super().get_fieldsets(request, obj)
        else:            
            return fieldsets
    

admin_user.register(User, UserEditAdmin)
admin_user.register(Group, GroupAdmin)