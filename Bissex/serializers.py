from rest_framework import serializers
from Bissex.models import model_Bissex_annee, model_Bissex_range

class BissexSerializer_year(serializers.ModelSerializer):
    class Meta:
        model = model_Bissex_annee
        fields = ['id', 'command_type', 'command_entry', 'command_result', 'command_error']

class BissexSerializer_range(serializers.ModelSerializer):
    class Meta:
        model = model_Bissex_range
        fields = ['id', 'command_type', 'command_entry', 'command_result', 'command_error']