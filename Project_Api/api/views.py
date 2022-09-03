from django.shortcuts import render
from django.views import View
from .models import Cliente
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.
class ClienteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        clientes = list(Cliente.objects.values())
        if len(clientes) > 0:
            datos = {'message': "Success", 'clientes': clientes}
        else:
            datos = {'message': "Clientes no encontrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(
                                documento=jd['documento']
                                ,tipo_documento=jd['tipo_documento']
                                ,nombre=jd['nombre']
                                ,genero=jd['genero']
                                ,email=jd['email']
                            )
        datos = {'message' : "Success"}
        return JsonResponse(datos)
    
    def put(self, request):
        jd = json.loads(request.body)
        print(jd)
        Cliente.objects.filter( pk = jd['id'] ).update(
                                documento=jd['documento']
                                ,tipo_documento=jd['tipo_documento']
                                ,nombre=jd['nombre']
                                ,genero=jd['genero']
                                ,email=jd['email']
                            )
        datos = {'message' : "Datos Actualizados Correctamente"}
        return JsonResponse(datos)
    
    def delete(self, request):
        jd = json.loads(request.body)
        Cliente.objects.filter(pk=jd['id']).delete()
        datos = {'message' : 'Cliente Eliminado'}
        return JsonResponse(datos)

    def getClient(self, id):
        cliente = list(Cliente.objects.filter( id = id ).values())
        if len(cliente) > 0:
            datos = { 'message': 'Success', 'cliente': cliente} 
        else:
            datos = {'message': 'Cliente no encontrado'}
        return JsonResponse(datos)