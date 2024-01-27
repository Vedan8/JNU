# myapi/serializers.py
from rest_framework import serializers
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ('id', 'category', 'image_field','description','name','itemname')

# Serializer for handling image uploads
class ImageUploadSerializer(serializers.Serializer):
    itemname=serializers.CharField()
    name=serializers.CharField()
    description=serializers.CharField()
    category=serializers.CharField()
    image_field = serializers.ImageField()
