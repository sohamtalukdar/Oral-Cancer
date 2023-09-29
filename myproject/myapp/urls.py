from django.urls import path
from .views import DetectView  # Import the correct view

urlpatterns = [
    path('detect/', DetectView.as_view(), name='detect_objects'),
]
