from django.urls import path

from . import viewsets


urlpatterns = [
    path('universidades/', viewsets.UniversidadListView.as_view()),
    path('universidad/<str:slug>/', viewsets.UniversidadRetrieveView.as_view()),
    path('aula/<str:slug>/', viewsets.AulaRetrieveView.as_view()),
]