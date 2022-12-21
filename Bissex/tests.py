from django.test import TestCase
from . import views
from rest_framework import response

class BissexTestCase(TestCase):
    def test_bissex_annee(self):
        print(Bissex_annee("2024"))
        self.assertEqual(Bissex_annee("2024") , '{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":"2024 est une année bissextile."}')
    #def test_bissex_range(self):
    
    #def test_bissex_history(self):
