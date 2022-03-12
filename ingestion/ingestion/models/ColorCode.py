from django.db import models
class ColorCode(models.Model):
    id = models.AutoField(primary_key=True)
    color_code = models.IntegerField()
    color_text=models.CharField(max_length=200)









