from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import Bissex
from .serializers import BissexSerializer
from datetime import datetime
import json
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

    bissex = Bissex(command_type="Bissex_Year", command_entry=date1, command_result=result, command_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")) #On serialize
    bissex.save()
    serializer = BissexSerializer(bissex)
    content = JSONRenderer().render(serializer.data) #On transforme le contenu en JSON
    return HttpResponse(content, content_type = 'application/json') #On envoie la réponse JSON
    
@csrf_exempt
#Bissextiles sur range (Endpoint 2)
def Bissex_range(request):
    try: 
        date1 = str(request.GET['year1']) #On récupère la première date
        date2 = str(request.GET['year2']) #On récupère la seconde date

        if re.search('[a-zA-Z]', date1) or re.search('.,[@_!#$%^&*()<>?/|}{~:]', date1) or re.search('[a-zA-Z]', date2) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date2): #Vérification des caractères interdits sur les deux dates
            result = "Format de date invalide (caractère invalide)."
        elif date1 == "" or date2 == "": #Vérification de la présence des dates
            result = "Format de date invalide (date non renseignée)."
        elif int(date1) >= int(date2): #Vérification que date1 < date2
            result = "Intervalle incorrect (première date supérieure ou égale à la deuxième)."
        else:
            list_date = range(int(date1),int(date2)) #On remplit une liste avec l'étendue des dates
            list_good = [] #Initialisation du tableau

            for ldate in list_date: #On parcoure toute la liste
                ldate = int(ldate)
                if (((ldate % 4) == 0 and (ldate % 100) != 0) or ((ldate % 400) == 0)): #On vérifie que l'année est bissextile
                    list_good.append(ldate) #Si l'année est bissextile, on l'ajoute au tableau
            
            if len(list_good) > 1: #Si il y a plus d'une année bissextile dans l'intervalle
                loopb = True
                for gdate in list_good:
                    if loopb:
                        result = str(gdate)
                    else:
                        result = result + ", " + str(gdate)
                    loopb = False
                result = result + " sont des années bissextiles."
            elif len(list_good) == 1: #Si il n'y a qu'une seule année bissextile dans l'intervalle
                result = str(list_good[0]) + " est une année bissextile."
            else: #Si il n'y a pas d'année bissextile dans le tableau
                result = "Aucune année n'est bissextile dans cet intervalle."
    except Exception:
        result = "Exception"
        date1 = "Erreur"
        date2 = "Erreur"
    bissex = Bissex(command_type="Bissex_Range", command_entry=date1 + " - " + date2, command_result=result, command_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")) #On serialize
    bissex.save()
    serializer = BissexSerializer(bissex)
    content = JSONRenderer().render(serializer.data) #On transforme le contenu en JSON
    return HttpResponse(content, content_type = 'application/json') #On envoie la réponse JSON

@csrf_exempt
#Historique des commandes (Endpoint 3)
def Bissex_history(request):
    result = {}
    all_bissex = Bissex.objects.all()
    for obj in all_bissex:
        result[obj.command_date] = [obj.command_type],[obj.command_entry],[obj.command_result]
    return HttpResponse(json.dumps(result), content_type = 'application/json')
    

