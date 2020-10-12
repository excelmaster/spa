from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from clientes.models import Clientes
from clientes.serializers import ClienteSerializer

from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == 'GET':
        print(clientess.objects.all())
        
        try:
          clientes = clientes.objects.all()
          clientes_serializer = ClienteSerializer(clientes, many=True)

          response = {
             'message': "Get all clientes'Infos Successfully",
             'clientes': clientes_serializer.data,
             'error': ""
          }
          return JsonResponse(response, status=status.HTTP_200_OK);
        except: 
          error = {
            'message': "Fail! -> can NOT get all the clientes List. Please check again!",
            'clientes': "[]",
            'error': "Error"
          }
          return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    elif request.method == 'POST':
        try:
            clientes_data = JSONParser().parse(request)
            clientes_serializer = clienteserializer(data=clientes_data)
            
            if clientes_serializer.is_valid():
                clientes_serializer.save()
                print(clientes_serializer.data)
                response = {
                   'message': "Successfully Upload a clientes with id = %d" % clientes_serializer.data.get('id'),
                   'clientes': [clientes_serializer.data],
                   'error': "" 
                }
                return JsonResponse(response, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'clientes':"[]",
                    'error': clientes_serializer.errors
                }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except: 
            exceptionError = {
                    'message': "Can Not upload successfully!",
                    'clientes': "[]",
                    'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR);

@csrf_exempt 
@api_view(['PUT', 'DELETE'])
def clientes_detail(request, pk):
    try: 
        clientes = clientes.objects.get(pk=pk)
    except clientes.DoesNotExist:
        exceptionError = {
            'message': "Not found a clientes with id = %s!" % pk,
            'clientes': "[]",
            'error': "404 Code - Not Found!"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT':
        try:
            clientes_data = JSONParser().parse(request)
            clientes_serializer = clienteserializer(clientes, data=clientes_data)

            if clientes_serializer.is_valid(): 
                clientes_serializer.save()
                response = {
                    'message': "Successfully Update a clientes with id = %s" % pk,
                    'clientes': [clientes_serializer.data],
                    'error': ""
                }                
                return JsonResponse(response) 

            response = {
                    'message': "Fail to Update a clientes with id = %s" % pk,
                    'clientes': [clientes_serializer.data],
                    'error': clientes_serializer.errors
                }
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST) 
        except:
            exceptionError = {
                'message': "Fail to update a clientes with id = %s!" % pk,
                'clientes': [clientes_serializer.data],
                'error': "Internal Error!"
            }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
 
    elif request.method == 'DELETE':
        print("Deleting a clientes with id=%s"%pk)
        clientes.delete() 
        clientes_serializer = clienteserializer(clientes) 
        response = {
                'message': "Successfully Delete a clientes with id = %s" % pk,
                'clientes': [clientes_serializer.data],
                'error': ""
            }
        return JsonResponse(response)