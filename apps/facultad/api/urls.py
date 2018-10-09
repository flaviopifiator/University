from django.urls import path

from . import viewsets


urlpatterns = [
    path('facultades/', viewsets.FacultadListView.as_view(), name='facultades'),
    path('facultad/<str:slug>/', viewsets.FacultadRetrieveView.as_view(), name='facultad-detail'),

    path('departamentos/', viewsets.DepartamentoFacultadListView.as_view(), name='departamentos'),
    path('departamento/<str:slug>/', viewsets.DepartamentoFacultadRetrieveView.as_view(), name='departamento-detail'),

    path('carreras/', viewsets.CarreraListView.as_view(), name='carreras'),
    path('carrera/<str:slug>/', viewsets.CarreraRetrieveView.as_view(), name='carrera-detail'),

    path('profesores/', viewsets.ProfesorListView.as_view(), name='profesores'),
    path('profesor/<str:slug>/', viewsets.ProfesorRetrieveView.as_view(), name='profesor-detail'),

    path('planesestudios/', viewsets.PlanEstudioListView.as_view(), name='planestudios'),
    path('planesestudio/<str:slug>/', viewsets.PlanEstudioRetrieveView.as_view(), name='planestudio-detail'),
    
]