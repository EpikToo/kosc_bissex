from rest_framework import serializers
from Bissex.models import Bissex_history

class BissexSerializer(serializers.Serializer):
    command_type = serializers.CharField
    command_entry = serializers.CharField
    command_result = serializers.CharField
    command_date = serializers.DateTimeField

    def create(self, validated_data):
        return Bissex_history.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.command_type = validated_data.get('command_type', instance.command_type)
        instance.command_entry = validated_data.get('command_entry', instance.command_entry)
        instance.command_result = validated_data.get('command_result', instance.command_result)
        instance.command_date = validated_data.get('command_date', instance.command_date)
        instance.save()
        return instance