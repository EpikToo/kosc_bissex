from django.test import TestCase
from datetime import datetime

class BissexTestCase(TestCase):

    def test_bissex_annee(self):
        response = self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":"2024 est une année bissextile."}')

    def test_bissex_range(self):
        response = self.client.get('/bissex_range/?year1=2020&year2=2030').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"2020 - 2030","command_result":"2020, 2024, 2028 sont des années bissextiles."}')

    def test_bissex_history(self):
        self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore") #On génère d'abord un objet pour peupler l'historique
        response = self.client.get('/bissex_history/').content.decode("utf8", "ignore")
        expected = '{"' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '":[["Bissex_Year"],["2024"],["2024 est une année bissextile."]]}'
        self.assertEqual(response,expected)