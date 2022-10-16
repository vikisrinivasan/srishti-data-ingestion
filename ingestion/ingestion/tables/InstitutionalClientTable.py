import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.InstitutionalClients import  InstitutionalClients

# Create the form class.
class InstitutionalClientsTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'InstitutionalClients'])
    class Meta:
        model = InstitutionalClients
        order_by='Date'
        attrs = {"class": "table table-bordered"}
