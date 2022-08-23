from django.shortcuts import render
from django.views import View
from .models import Cliente
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
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
        print(jd)
        Cliente.objects.create(documento=jd['documento'],tipo_documento=jd['tipo_documento'],nombre=jd['nombre'],genero=jd['genero'],acceptance_tm=jd['acceptance_tm'],email=jd['email'])
        datos = {'message' : "Success"}
        return JsonResponse(datos)
