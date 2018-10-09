from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import DistanceToPointFilter

from . import serializers
from .. import models


class FacultadListView(generics.ListAPIView):
    queryset = models.Facultad.objects.all()
    serializer_class = serializers.FacultadListSerializer


class FacultadRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Facultad
    serializer_class = serializers.FacultadSerializer


class DepartamentoFacultadListView(generics.ListAPIView):
    queryset = models.DepartamentoFacultad.objects.all()
    serializer_class = serializers.DepartamentoListSerializer


class DepartamentoFacultadRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.DepartamentoFacultad
    serializer_class = serializers.DepartamentoSerializer


class CarreraListView(generics.ListAPIView):
    queryset = models.Carrera.objects.all()
    serializer_class = serializers.CarreraListSerializer


class CarreraRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Carrera
    serializer_class = serializers.CarreraSerializer


class ProfesorListView(generics.ListAPIView):
    queryset = models.Profesor.activos.all()
    serializer_class = serializers.ProfesorListSerializer


class ProfesorRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Profesor.activos.all()
    serializer_class = serializers.ProfesorSerializer


class PlanEstudioListView(generics.ListAPIView):
    queryset = models.PlanEstudio.objects.all()
    serializer_class = serializers.PlanEstudioListSerializer


class PlanEstudioRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.PlanEstudio.objects.all()
    serializer_class = serializers.PlanEstudioSerializer