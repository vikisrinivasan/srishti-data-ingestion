from django.db import models
import datetime
from django.utils import timezone
class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name=models.CharField(max_length=50,help_text="Name of the contact")
    potential_lead=models.CharField(max_length=300, choices = (('Yes','Yes'),('No','No')),default='No',help_text="Contact is potential lead or not , default value is No")
    contact_created_date=models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc), blank=True,help_text="Potential contact created date")
    country_code=models.CharField(max_length=200,default='unknown',help_text="Country code of the contact")
    country=models.CharField(max_length=200,default='unknown',help_text="Country name of the contact")
    region=models.CharField(max_length=200,default='unknown',help_text="Region of the contact(e.g South, North)")
    state=models.CharField(max_length=200,default='unknown',help_text="State of the contact(e.g chennai, delhi)")
    city=models.CharField(max_length=200,default='unknown',help_text="Name of the contact")
    phone=models.CharField(max_length=200,default='unknown',help_text="Phone number")
    email=models.EmailField(help_text="Contact email id")
    last_inbound_contact_date=models.DateField(blank=True,help_text="last Inbound Sales contact date",default=datetime.datetime.now(tz=timezone.utc))
    last_outbound_contact_date=models.DateField(blank=True,help_text="last Outbound Sales contact date",default=datetime.datetime.now(tz=timezone.utc))
    last_contact_channel=models.CharField(default="call",max_length=200,help_text="last contact channel")
    type=models.CharField(default="Individual",max_length=200,help_text="Contact type (Individual or Redistributor)")
    photographerLevel=models.CharField(default='Professional',max_length=200,help_text="Photographer Level , Professional or Novice")
    category=models.CharField(default='Unknown',max_length=200,help_text="Category of photographer(Wedding etc)")

    def __str__(self):
        return self.contact_name





