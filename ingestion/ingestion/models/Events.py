import datetime

from django.db import models
from .utils.MasterData import City,Country

from django.utils.timezone import now
class Events(models.Model):
    objects = None
    Id = models.AutoField(primary_key=True)
    Date=models.DateField(default=datetime.date.today,help_text="Current Date ")
    EventKey=models.CharField(max_length=100,help_text="Unique Key to Identify the event ")
    Name=models.CharField(max_length=200,help_text="Event Name ")
    Type=models.CharField(max_length=200,help_text="Event Type ")
    Mode=models.CharField(max_length=200,help_text="Event Mode (Virtual or Physical) ")
    Venue=models.CharField(max_length=200,help_text="Venue Address ")
    StartDate=models.DateField( default=datetime.date.today,help_text="Start Date ")
    EndDate=models.DateField( default=datetime.date.today,help_text="End Date ")
    Partner=models.CharField(max_length=200,help_text="Comma seperated list of partners ")
    AffliateBrand=models.CharField(max_length=200,help_text="Primary Affliate Brand ")
    AffliateBrand1=models.CharField(max_length=200,help_text="Affliate Brand 2 ")
    AffliateBrand2=models.CharField(max_length=200,help_text="Affliate Brand 3")
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







