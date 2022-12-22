from django.test import TestCase
from .views import Bissex_annee
import rest_framework

class BissexTestCase(TestCase):
    def test_bissex_annee(self):

        print(Bissex_annee("2024").content)
        self.assertEqual(Bissex_annee("2024").content.decode("utf-8", "ignore"), '{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":"2024 est une année bissextile."}')
    #def test_bissex_range(self):
    
    #def test_bissex_history(self):
