from django.db import models
class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    item_id=models.ForeignKey('ItemMaster',on_delete=models.CASCADE)
    contact_id=models.ForeignKey('Contacts',on_delete=models.CASCADE)
    resdis_id=models.ForeignKey('ResDis',on_delete=models.CASCADE)


