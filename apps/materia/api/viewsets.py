from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .. import models


class MateriaListView(generics.ListAPIView):
    queryset = models.Materia.objects.all()
    serializer_class = serializers.MateriaListSerializer


class MateriaRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Materia.objects.all()
    serializer_class = serializers.MateriaSerializer
