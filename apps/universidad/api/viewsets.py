from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import DistanceToPointFilter

from . import serializers
from .. import models


class UniversidadListView(generics.ListAPIView):
    queryset = models.Universidad.objects.filter(nombre__icontains='Catamarca')
    serializer_class = serializers.UniversidadListSerializer


class UniversidadRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de Universidad
    '''
    lookup_field = 'slug'
    queryset = models.Universidad
    serializer_class = serializers.UniversidadSerializer


class AulaRetrieveView(generics.RetrieveAPIView):
    '''
    Detalle de Aula
    '''
    lookup_field = 'slug'
    queryset = models.Aula
    serializer_class = serializers.AulaSerializer

