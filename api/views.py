from  django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    def get(self, pk):
        try:
            queryset = Cliente.objects.filter(pk=pk)
            return queryset
        except Cliente.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        client = ClienteSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(client.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        client = self.get(pk)
        serializer = ClientSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(client.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        cliente = Cliente.objects.filter(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class CIIUViewSet(viewsets.ModelViewSet):
    queryset = CIIU.objects.all()
    serializer_class = CIIUSerializer

    def get(self, pk):
        try:
            queryset = CIIU.objects.filter(pk=pk)
            return queryset
        except CIIU.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        ciiu = CIIUSerializer(data=request.data)
        if ciiu.is_valid():
            ciiu.save()
            return Response(ciiu.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        ciiu = self.get(pk)
        serializer = ClientSerializer(data=request.data)
        if ciiu.is_valid():
            ciiu.save()
            return Response(ciiu.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        ciiu = CIIU.objects.filter(pk=pk)
        ciiu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class TributosViewSet(viewsets.ModelViewSet):
    queryset = Tributos.objects.all()
    serializer_class = TributosSerializer

    def get(self, pk):
        try:
            queryset = Tributos.objects.filter(pk=pk)
            return queryset
        except Tributos.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        tributos = TributosSerializer(data=request.data)
        if tributos.is_valid():
            tributos.save()
            return Response(tributos.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        tributos = self.get(pk)
        serializer = TributosSerializer(data=request.data)
        if tributos.is_valid():
            tributos.save()
            return Response(tributos.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tributos = Tributos.objects.filter(pk=pk)
        tributos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class ResponsabilidadFiscalViewSet(viewsets.ModelViewSet):
    queryset = Responsabilidad_Fiscal.objects.all()
    serializer_class = ResponsabilidadFiscalSerializer

    def get(self, pk):
        try:
            queryset = Responsabilidad_Fiscal.objects.filter(pk=pk)
            return queryset
        except Responsabilidad_Fiscal.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        responsabilidad = ResponsabilidadFiscalSerializer(data=request.data)
        if responsabilidad.is_valid():
            responsabilidad.save()
            return Response(responsabilidad.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        responsabilidad = self.get(pk)
        serializer = ResponsabilidadFiscalSerializer(data=request.data)
        if responsabilidad.is_valid():
            responsabilidad.save()
            return Response(responsabilidad.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        responsabilidad = Responsabilidad_Fiscal.objects.filter(pk=pk)
        responsabilidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class EstadoTramiteViewSet(viewsets.ModelViewSet):
    queryset = Estado_Tramite.objects.all()
    serializer_class = EstadoTramiteSerializer

    def get(self, pk):
        try:
            queryset = Estado_Tramite.objects.filter(pk=pk)
            return queryset
        except Estado_Tramite.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        estadoTramite = EstadoTramiteSerializer(data=request.data)
        if estadoTramite.is_valid():
            estadoTramite.save()
            return Response(estadoTramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        estadoTramite = self.get(pk)
        serializer = EstadoTramiteSerializer(data=request.data)
        if estadoTramite.is_valid():
            estadoTramite.save()
            return Response(estadoTramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        estadoTramite = Estado_Tramite.objects.filter(pk=pk)
        estadoTramite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class GestionServicioViewSet(viewsets.ModelViewSet):
    queryset = Gestion_Servicio.objects.all()
    serializer_class = GestionServicioSerializer

    def get(self, pk):
        try:
            queryset = Gestion_Servicio.objects.filter(pk=pk)
            return queryset
        except Gestion_Servicio.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        gestion = GestionServicioSerializer(data=request.data)
        if gestion.is_valid():
            gestion.save()
            return Response(gestion.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        gestion = self.get(pk)
        serializer = GestionServicioSerializer(data=request.data)
        if gestion.is_valid():
            gestion.save()
            return Response(gestion.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        gestion = Gestion_Servicio.objects.filter(pk=pk)
        gestion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class DetalleTramiteViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Tramite.objects.filter()
    serializer_class = DetalleTramiteSerializer
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_backends = [DjangoFilterBackend]
    search_fields = ('created_by')
    filterset_fields =['created_by','id_tramite'] 

    def get(self, pk):
        try:
            queryset = Tramite.objects.filter(pk=pk)
            return queryset
        except Tramite.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        detalle = DetalleTramiteSerializer(data=request.data)
        if detalle.is_valid():
            detalle.save()
            return Response(detalle.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        detalle = self.get(pk)
        serializer = DetalleTramiteSerializer(data=request.data)
        if detalle.is_valid():
            detalle.save()
            return Response(detalle.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        detalle = Detalle_Tramite.objects.filter(pk=pk)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class BlogContableViewSet(viewsets.ModelViewSet):
    queryset = Blog_Contable.objects.all()
    serializer_class = BlogContableSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    def get(self, pk):
        try:
            queryset = Blog_Contable.objects.filter(pk=pk)
            return queryset
        except Blog_Contable.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        blogContable = BlogContableSerializer(data=request.data)
        if blogContable.is_valid():
            blogContable.save()
            return Response(blogContable.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        blogContable = self.get(pk)
        serializer = BlogContableSerializer(data=request.data)
        if blogContable.is_valid():
            blogContable.save()
            return Response(blogContable.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        blogContable = Blog_Contable.objects.filter(pk=pk)
        blogContable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TipoTramiteViewSet(viewsets.ModelViewSet):
    queryset = Tipo_tramite.objects.all()
    serializer_class = TipoTramiteSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    def get(self, pk):
        try:
            queryset = Tipo_tramite.objects.filter(pk=pk)
            return queryset
        except Tipo_tramite.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        tipoTramite = TipoTramiteSerializer(data=request.data)
        if tipoTramite.is_valid():
            tipoTramite.save()
            return Response(tipoTramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        tipoTramite = self.get(pk)
        serializer = TipoTramiteSerializer(data=request.data)
        if tipoTramite.is_valid():
            tipoTramite.save()
            return Response(tipoTramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tipoTramite = Tipo_tramite.objects.filter(pk=pk)
        tipoTramite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class TramiteViewSet(viewsets.ModelViewSet):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer
    #filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['created_by'] 
    #permission_classes = [permissions.IsAuthenticated]
    
    def get(self, pk):
        try:
            queryset = Tramite.objects.filter(pk=pk)
            return queryset
        except Tramite.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        tramite = TramiteSerializer(data=request.data)
        if tramite.is_valid():
            tramite.save()
            return Response(tramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        tramite = self.get(pk)
        serializer = TramiteSerializer(data=request.data)
        if tramite.is_valid():
            tramite.save()
            return Response(tramite.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tramite = Tramite.objects.filter(pk=pk)
        tramite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  