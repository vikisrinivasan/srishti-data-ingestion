import datetime

from django.db import models
from .utils.MasterData import City,Country
from django.utils.timezone import now
class ServiceRequests(models.Model):
    objects=None
    Id=models.AutoField(primary_key=True)
    RequestDate = models.DateField( default=datetime.date.today, help_text="Request Date")
    Brand=models.CharField(max_length=500, help_text="Brand Enquired")
    Name=models.CharField(max_length=200, help_text="Name")
    RequestText=models.CharField(max_length=200, help_text="Request Text")
    Phone=models.IntegerField(max_length=200, help_text="Primary Phone")
    Email=models.EmailField(max_length=500, help_text="Primary Email Id")
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
    ClosedDate=models.DateField( default=datetime.date.today, blank=False, help_text="Request Closed Date")
    Resolution=models.BooleanField(default=True, help_text="Resolved or Not")
    ProductsEnquired=models.CharField(max_length=500, help_text="Products Enquired")
    ResolvedBy=models.CharField(max_length=100, help_text="Resolved By")
    ServiceCenter=models.CharField(max_length=200, help_text="Service Center")