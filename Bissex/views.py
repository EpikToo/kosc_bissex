from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import model_Bissex_annee, model_Bissex_range
from .serializers import BissexSerializer_year, BissexSerializer_range
import re

#Bissextile sur année (Endpoint 1)
@api_view(["GET"])
def Bissex_annee(request):
    try:    
        #On récupère la date
        date1 = str(request.GET['year'])
        
        #On regarde si une date à été donnée
        if date1 == "":
            result = ""
            error = "Année non renseignée."
        #On regarde si le format est valide
        elif re.search('[a-zA-Z]', date1) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date1):
            result = ""
            error = "Caractère(s) invalide(s)."
        
        else:
            #On passe la date en int pour effectuer des comparaisons
            dateint = int(date1)
            error = "OK"

            #On effectue le check si l'année est bissextile ou non
            if (((dateint % 4) == 0 and (dateint % 100) != 0) or ((dateint % 400) == 0)):
                result = True
            else:
                result = False
    
    except Exception:
        result = ""
        error = "Exception."
    
    #On serialize puis on envoie la réponse en JSON
    bissex = model_Bissex_annee(command_type="Bissex_Year", command_entry=date1, command_result=result, command_error=error)
    bissex.save()
    serializer = BissexSerializer_year(bissex)
    return Response(serializer.data)

#Bissextiles sur range (Endpoint 2)
@api_view(["GET"])
def Bissex_range(request):
    try: 
        #On récupère la première date
        date1 = str(request.GET['year1']) 
        date2 = str(request.GET['year2'])
        
         #Vérification de la présence des dates
        if date1 == "" or date2 == "":
            result = ""
            error = "Année(s) non-renseignée(s)."
            
        #Vérification des caractères interdits sur les deux dates
        elif re.search('[a-zA-Z]', date1) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date1) or re.search('[a-zA-Z]', date2) or re.search('[,.@_!#$%^&*()<>?/|}{~:]', date2):
            result = ""
            error = "Caractère(s) invalide(s)."

        #Vérification que date1 < date2
        elif int(date1) >= int(date2):
            result = ""
            error = "Intervalle incorrect (première date supérieure ou égale à la deuxième)."
        
        else:
             #On remplit une liste avec l'étendue des dates, on initialise des variables utiles
            list_date = range(int(date1),int(date2))
            result = "["
            error = "OK"
            bbool = True
    
            #On parcoure toute la liste où nn vérifie si l'année est bissextile
            for idate in list_date:
                if (((idate % 4) == 0 and (idate % 100) != 0) or ((idate % 400) == 0)):
                    if bbool:
                        result = result + str(idate)
                        bbool = False
                    else:
                        result = result + ", " + str(idate)
            result = result + "]"
    
    except Exception:
        result = ""
        error = "Exception."

    #On serialize et on envoie la réponse en JSON
    bissex = model_Bissex_range(command_type="Bissex_Range", command_entry=date1 + " - " + date2, command_result=result, command_error=error)
    bissex.save()
    serializer = BissexSerializer_range(bissex)
    return Response(serializer.data)

#Historique des commandes (Endpoint 3)
@api_view(["GET"])
def Bissex_history(request):
    #On initialise les tableaux dont on aura besoin
    result_annee = {}
    result_range = {}
    result_sorted = {}

    #On récupère les modèles
    Bissex_annee = model_Bissex_annee.objects.all()
    Bissex_range = model_Bissex_range.objects.all()

    #On forme les dictionnaires pour les fonctions annee et range
    for obj in Bissex_annee:
        result_annee[(obj.command_date).strftime("%d/%m/%Y %H:%M:%S")] = [obj.command_type],[obj.command_entry],[obj.command_result]
    for obj in Bissex_range:
        result_range[(obj.command_date).strftime("%d/%m/%Y %H:%M:%S")] = [obj.command_type],[obj.command_entry],[obj.command_result]
    
    #On fusionne les deux tableaux dans un seul
    result_temp = {**result_annee, **result_range}

    #On le trie
    for key in sorted(result_temp, reverse = True):
        result_sorted[key] = result_temp[key]
    
    return Response(result_sorted)
    

