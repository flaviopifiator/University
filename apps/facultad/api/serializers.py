from rest_framework import serializers

from apps.util.api import serializers as util_serializers

from .. import models


###################################################################### LISTS SERIALIZERS


class DepartamentoListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:departamento-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.DepartamentoFacultad
        fields = ('url', 'nombre',)
    

class FacultadListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:facultad-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.Facultad
        fields = ('url', 'nombre',)
       

class CarreraListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:carrera-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.Carrera
        fields = ('url', 'nombre',)


class ProfesorListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:profesor-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.Profesor
        fields = ('url', 'nombre_apellido',)


class PlanEstudioListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:planestudio-detail',
        lookup_field='slug'
    )
    carrera = serializers.StringRelatedField()

    class Meta:
        model = models.PlanEstudio
        fields = ('url', 'carrera', 'año',)


###################################################################### DETAILS SERIALIZERS


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartamentoFacultad
        exclude = ('id',)

    carreras = CarreraListSerializer(many=True, read_only=True)
    facultad = FacultadListSerializer(many=False, read_only=True)
    cargos = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.CargoSerializer
    )
    horarios = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.HorarioSerializer
    )
    emails = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.EmailSerializer
    )
    telefonos = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.TelefonoSerializer
    )

    redes_sociales = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.RedSocialSerializer
    )
 

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Facultad
        fields = (
            'slug', 'nombre', 'sigla', 'descripcion', 'siu',
            'aula_virtual', 'ubicacion', 'nombre_direccion',
            'numero_direccion', 'cargos', 'horarios', 'imagenes', 
            'emails', 'telefonos', 'redes_sociales', 'departamentos'
        )
    departamentos = DepartamentoListSerializer(
        many=True, read_only=True
    )
    cargos = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.CargoSerializer
    )
    horarios = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.HorarioSerializer
    )
    imagenes = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.ImagenSerializer
    )
    emails = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.EmailSerializer
    )
    telefonos = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.TelefonoSerializer
    )

    redes_sociales = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.RedSocialSerializer
    )


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrera
        exclude = ('id', )

    duracion = serializers.SerializerMethodField()
    tipo = serializers.SerializerMethodField()
    facultad = serializers.SerializerMethodField()
    departamento = serializers.StringRelatedField()
    
    def get_duracion(self, instance):
        return instance.get_duracion_display()

    def get_tipo(self, instance):
        return instance.get_tipo_display()

    def get_facultad(self, instance):
        return instance.departamento.facultad.nombre


class ProfesorSerializer(serializers.Serializer):
    class Meta:
        model = models.Profesor
        exclude = ('id', 'activo')
        fields = (
            'nombre', 'apellido',
        )

    nombre_apellido = serializers.CharField()
    telefonos = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.TelefonoSerializer
    )
    emails = util_serializers.GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=util_serializers.EmailSerializer
    )


class PlanEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanEstudio
        exclude = ('id', )

    carrera = serializers.StringRelatedField()