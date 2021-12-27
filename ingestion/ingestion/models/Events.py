from django.db import models
class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    code=models.IntegerField()
    event_name=models.CharField(max_length=200)
    event_type=models.CharField(max_length=200)
    event_date=models.DateTimeField()
    event_channel=models.CharField(max_length=200)
    event_city=models.CharField(max_length=200)
    event_country=models.CharField(max_length=200)






