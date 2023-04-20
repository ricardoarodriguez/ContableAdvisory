from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = [ 'url','id','documento','tipo_documento','nombre','genero','email','acceptance_tm','created_at','update_at', 'telefono','describe']

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

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = [ 'url','id','nombre','created_at','estado' ]

class GestionServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gestion_Servicio
        fields = [ 'url','id','observacion', 'id_servicio','id_estado_servicio','created_at','estado' ]

class BlogContableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog_Contable
        fields = [ 'url', 'id', 'title', 'subtitle','content','created_at','update_at']

class TipoTramiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_tramite
        fields = [ 'url', 'id', 'tipo_tramite', 'id_padre','nombre_padre','is_process','created_by','created_at','update_at','is_active']

class TramiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tramite
        fields = [ 'url', 'id', 'id_tipo_tramite', 'tipo_tramite', 'id_proceso','proceso','attached_file_path','created_by','created_at','id_estado','estado','is_active']

class DetalleTramiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle_Tramite
        fields = [ 'url', 'id', 'id_tramite', 'observaciones', 'id_servicio', 'attached_file_path','created_by','created_at','id_estado','estado','is_active']

class EstadoTramiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado_Tramite
        fields = [ 'url', 'id', 'nombre', 'created_by','created_at','is_active']
