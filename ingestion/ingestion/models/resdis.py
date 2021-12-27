from django.db import models

class ResDis(models.Model):
    resdis_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    contact_name=models.CharField(max_length=50)
    city_code=models.CharField(max_length=200)
    contact_phone=models.CharField(max_length=200)
    last_Inbound_contact_date=models.DateField()
    last_Outbound_contact_date=models.DateField()
    last_contact_channel=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    po_id=models.ForeignKey('ProductOffered',on_delete=models.CASCADE)