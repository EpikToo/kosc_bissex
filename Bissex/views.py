from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Bissex.models import Bissex
from Bissex.serializers import BissexSerializer



@csrf_exempt
#Bssextile sur année (Endpoint 1)
def Bissex_annee(request):
    template = loader.get_template('Bissex/Bissex_annee.html')
    return HttpResponse(template.render(request))


@csrf_exempt
#Bissextiles sur range (Endpoint 2)
def Bissex_range(request):
    yo = "o"

@csrf_exempt
#Historique des commandes (Endpoint 3)
def Bissex_history(request):
    if request.method == 'GET':
        Bissexs = Bissex.objects.all()
        serializer = BissexSerializer(Bissexs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BissexSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

