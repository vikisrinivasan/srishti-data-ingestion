from django.db import models
import datetime

from . import contacts
class ResDis(models.Model):
    resdis_id = models.AutoField(primary_key=True)
    name=models.CharField()
    contact_name=models.CharField(max_length=50)
    city_code=models.CharField()
    contact_phone=models.CharField()
    last_Inbound_contact_date=models.DateField()
    last_Outbound_contact_date=models.DateField()
    last_contact_channel=models.CharField()
    type=models.CharField()
    po_id=models.IntegerField()