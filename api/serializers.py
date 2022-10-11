from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = [ 'url','id','documento','tipo_documento','nombre','genero','email','acceptance_tm','created_at','update_at']

class CIIUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CIIU
        fields = [ 'url','id','codigo','nombre','estado','created_at','update_at' ]

class TributosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tributos
        fields = [ 'url','id','nombre','created_at','estado' ]

class ResponsabilidadFiscalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responsabilidad_Fiscal
        fields = [ 'url','id','nombre','created_at','estado' ]

class EstadoServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado_Servicio
        fields = [ 'url','id','nombre','created_at','estado' ]

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = [ 'url','id','nombre','created_at','estado' ]

class GestionServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gestion_Servicio
        fields = [ 'url','id','observacion', 'id_servicio','id_estado_servicio','created_at','estado' ]

class DetalleServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_Servicio
        fields = [ 'url','id','id_cliente', 'id_servicio','created_at','estado' ]
