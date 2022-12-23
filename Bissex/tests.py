from django.test import TestCase
from datetime import datetime

class BissexTestCase(TestCase):

    def test_bissex_annee(self):
        response = self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":"2024 est une année bissextile."}')

        response = self.client.get('/bissex_annee/?year=-2024').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":2,"command_type":"Bissex_Year","command_entry":"-2024","command_result":"-2024 est une année bissextile."}')

        response = self.client.get('/bissex_annee/?year=salut,,?').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":3,"command_type":"Bissex_Year","command_entry":"salut,,?","command_result":"Format de date invalide (caractère invalide)."}')    

        response = self.client.get('/bissex_annee/?year=').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":4,"command_type":"Bissex_Year","command_entry":"","command_result":"Format de date invalide (date non renseignée)."}')    
        
    def test_bissex_range(self):
        response = self.client.get('/bissex_range/?year1=2020&year2=2030').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"2020 - 2030","command_result":"2020, 2024, 2028 sont des années bissextiles."}')

        response = self.client.get('/bissex_range/?year1=-2030&year2=-2020').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":2,"command_type":"Bissex_Range","command_entry":"-2030 - -2020","command_result":"-2028, -2024 sont des années bissextiles."}')

        response = self.client.get('/bissex_range/?year1=salut&year2=???').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":3,"command_type":"Bissex_Range","command_entry":"salut - ???","command_result":"Format de date invalide (caractère invalide)."}')

        response = self.client.get('/bissex_range/?year1=&year2=').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":4,"command_type":"Bissex_Range","command_entry":" - ","command_result":"Format de date invalide (date non renseignée)."}')

        response = self.client.get('/bissex_range/?year1=2030&year2=2020').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":5,"command_type":"Bissex_Range","command_entry":"2030 - 2020","command_result":"Intervalle incorrect (première date supérieure ou égale à la deuxième)."}')

    def test_bissex_history(self):
        self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore") #On génère d'abord un objet pour peupler l'historique
        response = self.client.get('/bissex_history/').content.decode("utf8", "ignore")
        expected = '{"' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '":[["Bissex_Year"],["2024"],["2024 est une année bissextile."]]}'
        self.assertEqual(response,expected)
