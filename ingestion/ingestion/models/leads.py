from django.db import models
import datetime

from . import resdis
class Leads(models.Model):
    lead_id = models.AutoField(primary_key=True)
    lead_created_date=models.DateField(default=datetime.datetime.now, blank=True)
    lead_name=models.CharField(max_length=50)
    lead_type=models.DateField(default='Individual')
    lead_converted=models.BooleanField(default=False)
    lead_source=models.CharField(max_length=50)
    lead_owner=models.CharField()
    resdis_id=models.ForeignKey(resdis.ResDis,on_delete=models.CASCADE)