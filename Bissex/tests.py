from django.test import TestCase
from .views import Bissex_annee
import rest_framework

class BissexTestCase(TestCase):
    def test_bissex_annee(self):
        #RETIRER b DEVANT STRING 
        ctnt = Bissex_annee("2024").content
        ctnt1 = ctnt.removeprefix()
        self.assertEqual(str.removeprefix(Bissex_annee("2024").content) , '{"id":1,"command_type":"Bissex_Year","command_entry":"2024","command_result":"2024 est une année bissextile."}')
    #def test_bissex_range(self):
    
    #def test_bissex_history(self):
