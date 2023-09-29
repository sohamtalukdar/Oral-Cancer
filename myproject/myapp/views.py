# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.detect import YOLOv7Service

class DetectView(APIView):
    def post(self, request, *args, **kwargs):
        image = request.FILES.get('image')  # 'image' should be the key used in Postman
        if not image:
            return Response({'error': 'Image not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Initialize your service and get prediction
        detector = YOLOv7Service()
        result = detector.detect(image)
        
        return Response({'result': result}, status=status.HTTP_200_OK)
