from django.db import models
import datetime

class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    resdis_id=models.AutoField()
    lead_id=models.F(max_length=50)
    lead_type=models.DateField(default='Individual')
    lead_converted=models.BooleanField(default=False)
    lead_source=models.CharField(max_length=50)
    lead_owner=models.CharField()
