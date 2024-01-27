# myapi/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import YourModel
from .serializers import YourModelSerializer, ImageUploadSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter

class GetImageView(APIView):
    def get(self, request, pk):
        # Retrieve YourModel instance based on the provided ID (pk)
        your_model_instance = get_object_or_404(YourModel, pk=pk)

        # Serialize the instance to get the image URL
        serializer = YourModelSerializer(your_model_instance)
        image_url = serializer.data['image_field']

        # Open the image file and return it in the response
        with open(image_url.path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')  # Adjust content type based on your image format

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filter_backends=[SearchFilter]
    search_fields=['category']

class YouritemViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filter_backends=[SearchFilter]
    search_fields=['name']


class UploadImageView(generics.CreateAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Save the image file
            image_file = serializer.validated_data['image_field']
            category=serializer.validated_data['category']
            description=serializer.validated_data['description']
            name=serializer.validated_data['name']
            itemname=serializer.validated_data['itemname']
            your_model_instance = YourModel(image_field=image_file,category=category,description=description,name=name,itemname=itemname)
            your_model_instance.save()

            # Optionally, you may want to return the details of the created instance
            response_serializer = YourModelSerializer(your_model_instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
