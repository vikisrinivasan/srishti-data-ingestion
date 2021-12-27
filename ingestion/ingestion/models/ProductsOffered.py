from django.db import models

class ProductOffered(models.Model):
    po_id = models.AutoField(primary_key=True)
    product_category= models.CharField(max_length=200)




