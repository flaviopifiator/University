from rest_framework import serializers

from apps.util.api import serializers as util_serializers
from apps.facultad.api import serializers as facultad_serializers
from apps.universidad.api import serializers as universidad_serializers

from .. import models


###################################################################### LISTS SERIALIZERS


class MateriaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:materia-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.Materia
        fields = ('url', 'nombre', 'codigo',)
    

class ModoProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModoProfesor
        exclude = ('id', 'horario_materia')

    modo = serializers.SerializerMethodField()
    profesores = facultad_serializers.ProfesorSerializer(
        many=True, read_only=True
    )
    
    def get_modo(self, instance):
        return instance.get_modo_display()


class HorarioMateriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HorarioMateria
        exclude = ('id', 'materia')
    
    dias = serializers.MultipleChoiceField(choices=models.HorarioMateria.DIAS)
    aula = universidad_serializers.AulaSerializer(many=False, read_only=True)
    modo_profesores = ModoProfesorSerializer(many=False, read_only=True)


###################################################################### DETAILS SERIALIZERS


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        exclude = ('id',)

    año = serializers.SerializerMethodField()
    periodo = serializers.SerializerMethodField()
    correlativas_cursar = MateriaListSerializer(many=True, read_only=True)
    correlativas_aprobar = MateriaListSerializer(many=True, read_only=True)
    horarios = HorarioMateriaListSerializer(many=True, read_only=True)
    planes_estudio = facultad_serializers.PlanEstudioListSerializer(
        many=True, read_only=True
    )

    def get_año(self, instance):
        return instance.get_año_display()

    def get_periodo(self, instance):
        return instance.get_periodo_display()