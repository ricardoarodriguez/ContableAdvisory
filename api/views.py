from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
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

class EstadoServicioViewSet(viewsets.ModelViewSet):
    queryset = Estado_Servicio.objects.all()
    serializer_class = EstadoServicioSerializer

    def get(self, pk):
        try:
            queryset = Estado_Servicio.objects.filter(pk=pk)
            return queryset
        except Estado_Servicio.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        estadoServicio = EstadoServicioSerializer(data=request.data)
        if estadoServicio.is_valid():
            estadoServicio.save()
            return Response(estadoServicio.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        estadoServicio = self.get(pk)
        serializer = EstadoServicioSerializer(data=request.data)
        if estadoServicio.is_valid():
            estadoServicio.save()
            return Response(estadoServicio.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        estadoServicio = Estado_Servicio.objects.filter(pk=pk)
        estadoServicio.delete()
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

class DetalleServicioViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Servicio.objects.all()
    serializer_class = DetalleServicioSerializer

    def get(self, pk):
        try:
            queryset = Detalle_Servicio.objects.filter(pk=pk)
            return queryset
        except Detalle_Servicio.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        detalle = DetalleServicioSerializer(data=request.data)
        if detalle.is_valid():
            detalle.save()
            return Response(detalle.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        detalle = self.get(pk)
        serializer = DetalleServicioSerializer(data=request.data)
        if detalle.is_valid():
            detalle.save()
            return Response(detalle.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        detalle = Detalle_Servicio.objects.filter(pk=pk)
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