from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Bissex.models import Bissex
from Bissex.serializers import BissexSerializer

@csrf_exempt
#Historique des commandes
def Bissex_history(request):
    if request.method == 'GET':
        Bissex = Bissex.objects.all()
        serializer = BissexSerializer(Bissex, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BissexSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)