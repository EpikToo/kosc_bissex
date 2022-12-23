from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import model_Bissex_annee, model_Bissex_range
from .serializers import BissexSerializer_year, BissexSerializer_range
from datetime import datetime
import re

@api_view(["GET"])
#Bissextile sur année (Endpoint 1)
def Bissex_annee(request):
    try:    
        date1 = str(request.GET['year']) #On récupère la première date
        
        if date1 == "": #On regarde si une date à été donnée
            result = ""
            error = "Année non renseignée."
        elif re.search('[a-zA-Z]', date1) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date1): #On regarde si le format est valide
            result = ""
            error = "Caractère(s) invalide(s)."
        
        else:
            dateint = int(date1) #On passe la date en int pour effectuer des comparaisons
            error = "OK"
            if (((dateint % 4) == 0 and (dateint % 100) != 0) or ((dateint % 400) == 0)): #On effectue le check si l'année est bissextile ou non
                result = True
            else:
                result = False
    
    except Exception:
        result = ""
        error = "Exception."
    
    bissex = model_Bissex_annee(command_type="Bissex_Year", command_entry=date1, command_result=result, command_error=error) #On serialize
    bissex.save()
    serializer = BissexSerializer_year(bissex)
    return Response(serializer.data) #On envoie la réponse JSON

@api_view(["GET"])
#Bissextiles sur range (Endpoint 2)
def Bissex_range(request):
    try: 
        date1 = str(request.GET['year1']) #On récupère la première date
        date2 = str(request.GET['year2']) #On récupère la seconde date
        
        if date1 == "" or date2 == "": #Vérification de la présence des dates
            result = ""
            error = "Année(s) non-renseignée(s)."
        elif re.search('[a-zA-Z]', date1) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date1) or re.search('[a-zA-Z]', date2) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date2): #Vérification des caractères interdits sur les deux dates
            result = ""
            error = "Caractère(s) invalide(s)."
        elif int(date1) >= int(date2): #Vérification que date1 < date2
            result = ""
            error = "Intervalle incorrect (première date supérieure ou égale à la deuxième)."
        
        else:
            list_date = range(int(date1),int(date2)) #On remplit une liste avec l'étendue des dates
            #list_good = [] #Initialisation du tableau, voir PostGreSQL pour stocker des tableaux en modèle
            result = "["
            error = "OK"
            bbool = True
            for idate in list_date: #On parcoure toute la liste
                if (((idate % 4) == 0 and (idate % 100) != 0) or ((idate % 400) == 0)): #On vérifie que l'année est bissextile
                    if bbool:
                        result = result + str(idate)
                        bbool = False
                    else:
                        #list_good.append(ldate) #Si l'année est bissextile, on l'ajoute au tableau
                        result = result + ", " + str(idate)
            result = result + "]"
    
    except Exception:
        result = ""
        error = "Exception."
    
    bissex = model_Bissex_range(command_type="Bissex_Range", command_entry=date1 + " - " + date2, command_result=result, command_error=error) #On serialize
    bissex.save()
    serializer = BissexSerializer_range(bissex)
    return Response(serializer.data) #On envoie la réponse JSON

@api_view(["GET"])
#Historique des commandes (Endpoint 3)
def Bissex_history(request):
    result_annee = {}
    result_range = {}
    Bissex_annee = model_Bissex_annee.objects.all()
    Bissex_range = model_Bissex_range.objects.all()

    for obj in Bissex_annee:
        result_annee[(obj.command_date).strftime("%d/%m/%Y %H:%M:%S")] = [obj.command_type],[obj.command_entry],[obj.command_result]
    for obj in Bissex_range:
        result_range[(obj.command_date).strftime("%d/%m/%Y %H:%M:%S")] = [obj.command_type],[obj.command_entry],[obj.command_result]
    result = result_annee | result_range
    sorted(result.items(), reverse = True)
    return Response(sorted(result.items(), reverse = True))
    

