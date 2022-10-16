import datetime

from django.db import models
from .utils.MasterData import City,Country
from django.utils.timezone import now

class EventRegistration(models.Model):
    objects = None
    Id = models.AutoField(primary_key=True)
    Date=models.DateField(default=datetime.date.today,help_text="Current Date")
    EventName=models.CharField(max_length=500,help_text="Event Name")
    EventDate=models.DateField( default=datetime.date.today,help_text="Event Date")
    Name=models.CharField(max_length=500,help_text="Event Attender Name")
    Pro=models.BooleanField(default="True",help_text="Whether the photographer is a pro or not")
    Youtube=models.URLField(max_length=500,help_text="Youtube Link")
    Instagram=models.CharField(max_length=500,help_text="Instagram Link")
    Snapchat=models.CharField(max_length=500,help_text="Snapchat Link")
    Facebook=models.URLField(max_length=500,help_text="Facebook Link")
    Twitter=models.CharField(max_length=500,help_text="Twitter Link")
    LinkedIn=models.URLField(max_length=500,help_text="Linkedin Profile")
    Phone=models.IntegerField(max_length=20,help_text="Contact Number Home")
    Phone1=models.IntegerField(max_length=20,help_text="Contact Number Office")
    Phone2=models.IntegerField(max_length=20,help_text="Contact Number Mobile")
    Email=models.EmailField(max_length=100,help_text="Primary Email ID")
    Email1=models.EmailField(max_length=100,help_text="Secondary Email ID")
    Email2=models.EmailField(max_length=100,help_text="Alternative Email ID")
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
    PermissionToShareData=models.BooleanField(default="True",help_text="Whether the attender has given permission to share data")
    Photographer=models.BooleanField(default="True",help_text="Whether attender is a photographer or not")
    GenreTags=models.CharField(max_length=100,help_text="Genre Tags")







