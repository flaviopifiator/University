#from django import forms
#from django import forms
#
#from dal import autocomplete
#from mapwidgets.widgets import GooglePointFieldWidget
#
#from . import models
#
#
#class UniversidadForm(forms.ModelForm):
#    class Meta:
#        model = models.Universidad
#        fields = '__all__'
#        widgets = {
#            'ubicacion': GooglePointFieldWidget,
#            #'departamento': autocomplete.ModelSelect2(
#            #    url='util:departamento-autocomplete',
#            #    forward=['departamento__provincia', ]
#            #),
#            #'localidad': autocomplete.ModelSelect2(
#            #    url='util:localidad-autocomplete',
#            #    forward=['departamento', ]
#            #),
#        }
#
#
#class AulaForm(forms.ModelForm):
#    class Meta:
#        model = models.Aula
#        fields = '__all__'
#        widgets = {
#            'ubicacion': GooglePointFieldWidget,
#        }
#