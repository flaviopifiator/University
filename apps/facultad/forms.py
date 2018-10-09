from django import forms
from dal import autocomplete

#from apps.core.widgets import GMapPointWidget
#from . import models
#
#
#class FacultadForm(forms.ModelForm):
#    class Meta:
#        model = models.Facultad
#        fields = '__all__'
#        widgets = {
#            'ubicacion': GMapPointWidget(),
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
#class DepartamentoFacultadForm(forms.ModelForm):
#    class Meta:
#        model = models.DepartamentoFacultad
#        fields = '__all__'
#        widgets = {
#            'ubicacion': GMapPointWidget(),
#            #'departamento': autocomplete.ModelSelect2(
#            #    url='util:departamento-autocomplete',
#            #    forward=['departamento__provincia', ]
#            #),
#            #'localidad': autocomplete.ModelSelect2(
#            #    url='util:localidad-autocomplete',
#            #    forward=['departamento', ]
#            #),
#        }