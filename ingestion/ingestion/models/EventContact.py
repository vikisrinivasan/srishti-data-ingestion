from django.db import models

class EventContact(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('Events',on_delete=models.CASCADE)
    contact_id=models.ForeignKey('Contacts',on_delete=models.CASCADE)









