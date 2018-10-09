from rest_framework import serializers

from apps.util.api import serializers as util_serializers

from .. import models


class UniversidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Universidad
        fields = ('slug', 'nombre',)

        
class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Universidad
        fields = '__all__'

    facultades = serializers.SlugRelatedField(many=True, slug_field="slug", read_only=True)
    pais = serializers.StringRelatedField(many=False)        
    provincia = serializers.StringRelatedField(many=False)
    departamento = serializers.StringRelatedField(many=False)
    localidad = serializers.StringRelatedField(many=False)

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
    

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aula
        fields = (
            'nombre', 'descripcion',
            'ubicacion'
        )