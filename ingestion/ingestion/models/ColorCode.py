from django.db import models
import datetime
from .leads import Leads
from .resdis import ResDis
from . import Events
from . import contacts
class ColorCode(models.Model):
    id = models.AutoField(primary_key=True)
    color_code = models.IntegerField()
    color_text=models.CharField(max_length=200)









