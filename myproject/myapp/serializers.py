from dataclasses import field
from email.mime import image
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from myapp.models import OCImage


class ImgRecSerializer(serializers.ModelSerializer):

    RecognitionImg = Base64ImageField()
    class Meta:
        model = OCImage
        fields = '__all__'
    def create(self,validate_data):
        # Organization_ID = validate_data.pop('RecognitionID')
        # face_id = validate_data.pop('PersonID')
        RecognitionImg = validate_data.pop('RecognitionImg')

        return OCImage.objects.create(RecognitionImg=RecognitionImg)