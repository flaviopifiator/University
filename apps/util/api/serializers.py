from rest_framework import serializers

from apps.universidad.models import Universidad

from .. import models


############################################################## GENERICS
class GenericRelatedField(serializers.RelatedField):
    """
    GenericRelations -> Modelos genéricos.
    Simple y sencillo ...
    """
    def __init__(self, **kw):
        self.serializer_class = kw.pop('serializer_class', None)
        super().__init__(**kw)

    def to_representation(self, instance):
        if not self.serializer_class:
            raise Exception('No se definió el serializer_class')

        return self.serializer_class(instance).data


class CargoSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = models.Cargo
        fields = ('nombre', 'prioridad', 'autoridades',)
    
    autoridades = serializers.StringRelatedField(many=True)


class HorarioSerializer(serializers.Serializer):
    """
    """
    class Meta:
        model = models.Horario
        fields = ('turno', 'inicio', 'fin', 'dias')
    
    turno = serializers.SerializerMethodField()
    dias = serializers.MultipleChoiceField(choices=models.Horario.DIAS)
    
    def get_turno(self, instance):
        return instance.get_turno_display()
    

class TelefonoSerializer(serializers.ModelSerializer):
    """
    Documentación: 
    """

    class Meta:
        model = models.Telefono
        fields = ('tipo', 'numero',)

    tipo = serializers.SerializerMethodField()

    def get_tipo(self, instance):
        return instance.get_tipo_display()


class EmailSerializer(serializers.ModelSerializer):
    """
    Documentación: 
    """

    class Meta:
        model = models.Email
        fields = ('email',)


class RedSocialSerializer(serializers.ModelSerializer):
    """ Documentación: """
    class Meta:
        model = models.RedSocial
        fields = ('red', 'url',)

    red = serializers.SerializerMethodField()

    def get_red(self, instance):
        return instance.get_red_display()


class ImagenSerializer(serializers.ModelSerializer):
    """ Documentación: """
    class Meta:
        model = models.Imagen
        fields = ('imagen', 'portada',)


############################################################## ABSTRACT

class PersonaSerializer(serializers.Serializer):
    """
    """
    class Meta:
        fields = (
            'nombre', 'apellido'
        )

    telefonos = GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=TelefonoSerializer
    )
    emails = GenericRelatedField(
        read_only=True,
        many=True,
        serializer_class=EmailSerializer
    )


class DireccionSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        fields = (
            'nombre_direccion', 'numero_direccion',
            'extra', 'pais', 'provincia', 
            'departamento', 'localidad',
        )

############################################################# MODELS

class AutoridadSerializer(PersonaSerializer):
    class Meta:
        model = models.Autoridad
        fields = ('pk', 'titulo', 
            'titulo_nombre') + PersonaSerializer.Meta.fields


'''
class LocalidadSerializer(serializers.ModelSerializer):
    """
    Documentación: 
    """
    class Meta:
        model = models.Localidad
        fields = ('pk', 'nombre', 'departamento')

    departamento = serializers.StringRelatedField(many=False)


class DepartamentoSerializer(serializers.ModelSerializer):
    """
    Documentación:
    """
    class Meta:
        model = models.Departamento
        fields = (
            'pk', 'nombre', 'provincia'
        )


class ProvinciaSerializer(serializers.ModelSerializer):
    """
    Documentación:
    """
    class Meta:
        model = models.Provincia
        fields = (
            'pk', 'nombre', 'pais'
        )
'''
