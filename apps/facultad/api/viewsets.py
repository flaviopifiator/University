from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import DistanceToPointFilter

from . import serializers
from .. import models


class FacultadListView(generics.ListAPIView):
    '''
    Listado de Facultades
    '''
    queryset = models.Facultad.objects.all()
    serializer_class = serializers.FacultadListSerializer


class FacultadRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de Facultad
    '''
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Facultad
    serializer_class = serializers.FacultadSerializer


class DepartamentoFacultadListView(generics.ListAPIView):
    '''
    Listado de Departamentos
    '''
    queryset = models.DepartamentoFacultad.objects.all()
    serializer_class = serializers.DepartamentoListSerializer


class DepartamentoFacultadRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de un Departamento de una Facultad
    '''
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.DepartamentoFacultad
    serializer_class = serializers.DepartamentoSerializer


class CarreraListView(generics.ListAPIView):
    '''
    Listado de Carreras
    '''
    queryset = models.Carrera.objects.all()
    serializer_class = serializers.CarreraListSerializer


class CarreraRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de una Carrera
    '''
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Carrera
    serializer_class = serializers.CarreraSerializer


class ProfesorListView(generics.ListAPIView):
    '''
    Listado de Profesores Activos
    '''
    queryset = models.Profesor.activos.all()
    serializer_class = serializers.ProfesorListSerializer


class ProfesorRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de un Profesor
    '''
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Profesor.activos.all()
    serializer_class = serializers.ProfesorSerializer


class PlanEstudioListView(generics.ListAPIView):
    '''
    Listado de Planes de Estudio
    '''
    queryset = models.PlanEstudio.objects.all()
    serializer_class = serializers.PlanEstudioListSerializer


class PlanEstudioRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de un Plan de Estudio
    '''
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.PlanEstudio.objects.all()
    serializer_class = serializers.PlanEstudioSerializer