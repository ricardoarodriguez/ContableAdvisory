from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = [ 'url','id','documento','tipo_documento','nombre','genero','email','acceptance_tm','created_at','update_at']
