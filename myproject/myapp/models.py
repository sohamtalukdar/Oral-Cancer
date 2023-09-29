from django.db import models
import os

def upload_to(instance, filename):
    return os.path.join('uploads', filename)

class OCImage(models.Model):
    RecognitionImg = models.FileField(blank=False, null=False, upload_to=upload_to)
    
    def __str__(self):
        return str(self.RecognitionImg)
