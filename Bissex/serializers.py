from rest_framework import serializers
from Bissex.models import Bissex

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bissex
        fields = ['id', 'command_type', 'command_entry', 'command_result', 'command_date']