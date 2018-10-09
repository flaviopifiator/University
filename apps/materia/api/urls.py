from django.urls import path

from . import viewsets


urlpatterns = [
    path('materias/', viewsets.MateriaListView.as_view(), name='materias'),
    path('materia/<str:slug>/', viewsets.MateriaRetrieveView.as_view(), name='materia-detail'),

]