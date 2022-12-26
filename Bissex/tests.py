from django.test import TestCase
from datetime import datetime

class BissexTestCase(TestCase):

    def test_bissex_annee_good(self):
        response = self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":true,"command_error":"OK"}')

    def test_bissex_annee_goodminus(self):
        response = self.client.get('/bissex_annee/?year=-2024').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"-2024","command_result":true,"command_error":"OK"}')

    def test_bissex_annee_badchar(self):
        response = self.client.get('/bissex_annee/?year=salut,,?').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"salut,,?","command_result":null,"command_error":"Caractère(s) invalide(s)."}')    

    def test_bissex_annee_empty(self):
        response = self.client.get('/bissex_annee/?year=').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Year","command_entry":"","command_result":null,"command_error":"Année non renseignée."}')    
    


    def test_bissex_range_good(self):
        response = self.client.get('/bissex_range/?year1=2020&year2=2030').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"2020 - 2030","command_result":"[2020, 2024, 2028]","command_error":"OK"}')

    def test_bissex_range_goodminus(self):
        response = self.client.get('/bissex_range/?year1=-2030&year2=-2020').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"-2030 - -2020","command_result":"[-2028, -2024]","command_error":"OK"}')

    def test_bissex_range_badchar(self):
        response = self.client.get('/bissex_range/?year1=salut&year2=???').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"salut - ???","command_result":"","command_error":"Caractère(s) invalide(s)."}')

    def test_bissex_range_empty(self):
        response = self.client.get('/bissex_range/?year1=&year2=').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":" - ","command_result":"","command_error":"Année(s) non-renseignée(s)."}')

    def test_bissex_range_notsup(self):
        response = self.client.get('/bissex_range/?year1=2030&year2=2020').content.decode("utf8", "ignore")
        self.assertEqual(response,'{"id":1,"command_type":"Bissex_Range","command_entry":"2030 - 2020","command_result":"","command_error":"Intervalle incorrect (première date supérieure ou égale à la deuxième)."}')



    def test_bissex_history(self):
        self.client.get('/bissex_annee/?year=2024').content.decode("utf8", "ignore") 
        response = self.client.get('/bissex_history/').content.decode("utf8", "ignore")
        expected = '{"' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '":[["Bissex_Year"],["2024"],[true]]}'
        self.assertEqual(response,expected)