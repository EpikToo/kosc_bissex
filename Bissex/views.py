from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from Bissex.models import Bissex
from Bissex.serializers import BissexSerializer
from datetime import date
import re

@csrf_exempt
#Bissextile sur année (Endpoint 1)
def Bissex_annee(request):
    try:
        date1 = str(request.GET['year']) #Récupération de la date
        if date1 == "": #On regarde si une date à été donnée
            result = "Format de date invalide (date non renseignée)."
        elif re.search('[a-zA-Z]', date1) or re.search(',.[@_!#$%^&*()<>?/|}{~:]', date1): #On regarde si le format est valide
            result = "Format de date invalide (caractère invalide)."
        else:
            dateint = int(date1) #On passe la date en int pour effectuer des comparaisons
            if (((dateint % 4) == 0 and (dateint % 100) != 0) or ((dateint % 400) == 0)): #On effectue le check si l'année est bissextile ou non
                result = date1 + " est une année bissextile."
            else:
                result = date1 + " n'est pas une année bissextile."
    
    except Exception:
        result = "Exception"
        date1= "Erreur"

    bissex = Bissex(command_type="Bissex_Year", command_entry=date1, command_result=result, command_date=date.today())
    bissex.save()
    serializer = BissexSerializer(bissex)
    content= JSONRenderer().render(serializer.data)
    return HttpResponse(content)
    
@csrf_exempt
#Bissextiles sur range (Endpoint 2)
def Bissex_range(request):
    try: 
        date1 = str(request.GET['year1'])
        date2 = str(request.GET['year2'])

        if re.search('[a-zA-Z]', date1) or re.search('.,[@_!#$%^&*()<>?/|}{~:]', date1) or re.search('[a-zA-Z]', date2) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date2):
            result = "Format de date invalide (caractère invalide)."
        elif date1 == "" or date2 == "": #On regarde si une date à été donnée
            result = "Format de date invalide (date non renseignée)."
        elif int(date1) >= int(date2):
            result = "Intervalle incorrect (première date supérieure ou égale à la deuxième)."
        else:
            list_date = range(int(date1),int(date2))
            list_good = []

            for ldate in list_date:
                ldate = int(ldate)
                if (((ldate % 4) == 0 and (ldate % 100) != 0) or ((ldate % 400) == 0)): #On vérifie que l'année est bissextile
                    list_good.append(ldate)
            
            if len(list_good) > 1:
                loopb = True
                for gdate in list_good:
                    if loopb:
                        result = str(gdate)
                    else:
                        result = result + ", " + str(gdate)
                    loopb = False
                result = result + " sont des années bissextiles."
            elif len(list_good) == 1:
                result = str(list_good[0]) + " est une année bissextile."
            else:
                result = "Aucune année n'est bissextile dans cet intervalle."
    except Exception:
        result = "Exception"
        date1 = "Erreur"
        date2 = "Erreur"
    bissex = Bissex(command_type="Bissex_Range", command_entry=date1 + " - " + date2, command_result=result, command_date=date.today())
    bissex.save()
    serializer = BissexSerializer(bissex)
    content= JSONRenderer().render(serializer.data)
    return HttpResponse(content)




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

