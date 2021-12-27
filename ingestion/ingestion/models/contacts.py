from django.db import models
import datetime
class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    resdis_id=models.ForeignKey('ResDis',on_delete=models.CASCADE)
    lead_id=models.ForeignKey('Leads',on_delete=models.CASCADE)
    contact_name=models.CharField(max_length=50,help_text="Name of the contact")
    contact_created_date=models.DateTimeField(default=datetime.datetime.now, blank=True,help_text="Potential contact created date")
    country_code=models.CharField(max_length=200,default='unknown',help_text="Country code of the contact")
    country=models.CharField(max_length=200,default='unknown',help_text="Country name of the contact")
    region=models.CharField(max_length=200,default='unknown',help_text="Region of the contact(e.g South, North)")
    state=models.CharField(max_length=200,default='unknown',help_text="State of the contact(e.g chennai, delhi)")
    city=models.CharField(max_length=200,default='unknown',help_text="Name of the contact")
    phone=models.CharField(max_length=200,default='unknown',help_text="Phone number")
    email=models.EmailField(help_text="Contact email id")
    last_inbound_contact_date=models.DateField(blank=True,help_text="last Inbound Sales contact date")
    last_outbound_contact_date=models.DateField(blank=True,help_text="last Outbound Sales contact date")
    last_contact_channel=models.CharField(default="call",max_length=200,help_text="last contact channel")
    type=models.CharField(default="Individual",max_length=200,help_text="Contact type (Individual or Redistributor)")
    photographerLevel=models.CharField(default='Professional',max_length=200,help_text="Photographer Level , Professional or Novice")
    category=models.CharField(default='Unknown',max_length=200,help_text="Category of photographer(Wedding etc)")
    company_name=models.CharField(default='Unknown',max_length=200,help_text="Company Name")
    camera_id=models.ForeignKey('CameraDetails',on_delete=models.CASCADE)






