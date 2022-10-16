import datetime

from django.db import models
from .utils.MasterData import InstitutionType,City,Country
from django.utils.timezone import now
class InstitutionalClients(models.Model):
    objects=None
    Id = models.AutoField(primary_key=True)
    Date=models.DateField( default=datetime.date.today,help_text="Date")
    Name=models.CharField(max_length=500,help_text="Client Name")
    Contact=models.CharField(max_length=500,help_text="Primary Contact Name")
    Contact1=models.CharField(max_length=500,help_text="Secondary Contact Name")
    Contact2=models.CharField(max_length=500,help_text="Tertiary Contact Name")
    InstitutionType=models.CharField(  max_length=100,
                                       choices=InstitutionType.choices,
                                       default=InstitutionType.ProfessionalAcademy,help_text="Institution Type (Educational,"
                                                                                             "ProfessionalAcademy,"
                                                                                             "Reseller,Distributor)")
    Phone=models.IntegerField(max_length=20,help_text="Primary Contact Number")
    Phone1=models.IntegerField(max_length=20,help_text="Secondary Contact Number")
    Phone2=models.IntegerField(max_length=20,help_text="Tertiary Contact Number")
    Email=models.EmailField(max_length=100,help_text="Primary Email Id")
    Email1=models.EmailField(max_length=100,help_text="Secondary Email Id")
    Email2=models.EmailField(max_length=100,help_text="Tertiary Email Id")

    Website=models.URLField(default=False,help_text="Website Link")
    Address=models.CharField(max_length=100,default=False,help_text="Address")
    City = models.CharField(
        max_length=100,
        choices=City.choices,
        default=City.Delhi,
        help_text="City"
    )
    Country = models.CharField(
        max_length=100,
        choices=Country.choices,
        default=Country.INDIA,
        help_text="Country"
    )
    Products=models.CharField(max_length=500,    help_text="Products Owned")








