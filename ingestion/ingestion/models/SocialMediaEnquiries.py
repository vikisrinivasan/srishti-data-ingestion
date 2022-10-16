import datetime

from django.db import models
from .utils.MasterData import Platforms,City,Country
from django.utils.timezone import now
class SocialMediaEnquiries(models.Model):
    objects=None
    Id=models.AutoField(primary_key=True)
    ReceivedDate = models.DateField( default=datetime.date.today, help_text="Enquiry Received Date")
    Platform = models.CharField(
        max_length=100,
        choices=Platforms.choices,
        default=Platforms.INSTAGRAM
        , help_text="Platform (FACEBOOK,INSTAGRAM,WHATSAPP,LINKEDIN SNAPCHAT TWITTER)")
    ProfileURL=models.URLField(max_length=200, help_text="Profile URL")
    SocialProfile=models.CharField(max_length=200, help_text="Social Profile")
    Name=models.CharField(max_length=200, help_text="Name")
    EnquiryText=models.CharField(max_length=200, help_text="Enquiry Text ")
    Phone=models.IntegerField(max_length=200, help_text="Primary Phone Number")
    Email=models.EmailField(max_length=500, help_text="Email Id")
    City = models.CharField(
        max_length=100,
        choices=City.choices,
        default=City.Delhi
        , help_text="City"
    )
    Country = models.CharField(
        max_length=100,
        choices=Country.choices,
        default=Country.INDIA
        , help_text="Country"
    )
    ResponseDate=models.DateField( default=datetime.date.today, blank=True, help_text="Response Received Date")
    Resolution=models.BooleanField(default=True, help_text="Resolved or not")
    ResolvedFlag=models.BooleanField(default=True, help_text="Resolved Flag")
    ProductsEnquired=models.CharField(max_length=500, help_text="Products Enquired")
    ProductsSuggested=models.CharField(max_length=500, help_text="Products Suggested")








