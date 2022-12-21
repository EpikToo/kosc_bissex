from rest_framework import serializers
from Bissex.models import Bissex

class BissexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bissex
        fields = ['id', 'command_type', 'command_entry', 'command_result']