from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Bissex.models import Bissex
from Bissex.serializers import BissexSerializer
import re
#test branche 

@csrf_exempt
#Bissextile sur année (Endpoint 1)
def Bissex_annee(request):
    template = loader.get_template('Bissex/Bissex_annee.html')
    
    #Récupération de la date
    txtbx = request.POST['year']
    date = str(txtbx)

    #1. On regarde si la textbox à été remplie
    if date == "":
        result = {"bissex": "Renseignez une date (yyyy):"}
        return HttpResponse(template.render(result))

    #2. On regarde si le format est valide
    elif re.search('[a-zA-Z]', date) or re.search('[@_!#$%^&*()<>?/|}{~:]', date):
        result = {"bissex": "Merci de renseigner une date valide."}
        return HttpResponse(template.render(result))

    #3. Sinon c'est valide
    else:
        #Check si l'année est bissextile
        dateint = int(date)
        if (((dateint % 4) == 0 and (dateint % 100) != 0) or ((dateint % 400) == 0)):
            result = {"bissex": date + " est une année bissextile."}
        else:
            result = {"bissex": txtbx + " n'est pas une année bissextile."}

        #Envoi du résultat vers le front
        return HttpResponse(template.render(result))

@csrf_exempt
#Bissextiles sur range (Endpoint 2)
def Bissex_range(request):
    template = loader.get_template('Bissex/Bissex_range.html')
    return HttpResponse(template.render())

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

