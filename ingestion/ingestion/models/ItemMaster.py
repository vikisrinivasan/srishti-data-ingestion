from django.db import models

class ItemMaster(models.Model):
    id = models.AutoField(primary_key=True)
    category=models.IntegerField()
    name=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    brand=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    height=models.IntegerField()
    weight=models.IntegerField()
    breadth=models.IntegerField()
    length=models.IntegerField()
    color_code=models.ForeignKey('ColorCode',on_delete=models.CASCADE)
    material=models.CharField(max_length=200)
    total_available_qty=models.IntegerField()








