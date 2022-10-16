import datetime

from django.db import models
from .utils.MasterData import City,Country
from django.utils.timezone import now
class Influencers(models.Model):
    objects = None
    Id = models.AutoField(primary_key=True)
    Date= models.DateField(default=datetime.date.today,help_text="Date")
    Youtube=models.URLField(max_length=500,help_text="Youtube Link")
    Instagram=models.CharField(max_length=500,help_text="Instagram Link")
    Snapchat=models.CharField(max_length=500,help_text="Snapchat Link")
    Facebook=models.URLField(max_length=500,help_text="Facebook Link")
    Twitter=models.CharField(max_length=500,help_text="Twitter Link")
    LinkedIn=models.URLField(max_length=500,help_text="LinkedIn Link")
    Website=models.URLField(max_length=500,help_text="Website Link")
    Youtube_Followers=models.IntegerField(help_text="Youtube Followers")
    Instagram_Followers=models.IntegerField(help_text="Instagram Followers")
    Snapchat_Followers=models.IntegerField(help_text="Snapchat Followers")
    Twitter_Followers=models.IntegerField(help_text="Twitter Followers")
    LinkedInUrl_Followers=models.IntegerField(help_text="Linkedin Followers")
    Name=models.CharField(max_length=500,help_text="Influencer Name")
    Phone=models.IntegerField(max_length=20,help_text="Primary Phone Number")
    Phone1=models.IntegerField(max_length=20,help_text="Secondary Phone Number")
    Phone2=models.IntegerField(max_length=20,help_text="Tertiary Phone Number")
    Email=models.EmailField(max_length=100,help_text="Primary Email Id")
    Email1=models.EmailField(max_length=100,help_text="Secondary Email Id")
    Email2=models.EmailField(max_length=100,help_text="Tertiary Email Id")
    ProductOwned=models.CharField(max_length=100,help_text="Current Products Owned")
    City = models.CharField(
        max_length=100,
        choices=City.choices,
        default=City.Delhi,
        help_text="Select City"
    )
    Country = models.CharField(
        max_length=100,
        choices=Country.choices,
        default=Country.INDIA,
        help_text="Select Country"
    )
    GenreTags=models.CharField(max_length=100,help_text="Unique Genre Tags like (Wedding, Wildlife etc)")
    GenreKey=models.CharField(max_length=500,default=True,help_text="Unique Genre Keys to identify each genre uniquely")









