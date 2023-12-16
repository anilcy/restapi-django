from rest_framework import serializers
from rest.models import taskManager

class restSerializer(serializers.Serializer):
    
    title = serializers.CharField(read_only=True)
    description=serializers.CharField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    is_completed=serializers.BooleanField()

    def create(self, validated_data):
        return taskManager.objects.create(**validated_data)

    def update(self, validated_data, instance):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at= validated_data.get('updated_at', instance.updated_at)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance