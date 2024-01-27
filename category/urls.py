# myapi/urls.py
from django.urls import path
from .views import YourModelViewSet, UploadImageView, GetImageView,YouritemViewSet

urlpatterns = [
    path('your-model/', YourModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='your-model-list'),
    path('your-model/<int:pk>/', YourModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='your-model-detail'),
    path('upload-image/', UploadImageView.as_view(), name='upload-image'),
    path('get-image/<int:pk>/', GetImageView.as_view(), name='get-image'),
    path('your-items/',YouritemViewSet.as_view({'get': 'list', 'post': 'create'}),name='your-items')
]
