from django.db import models
class CameraDetails(models.Model):
    camera_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=200)
    weight=models.FloatField()





