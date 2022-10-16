import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.Events import  Events

# Create the form class.
class EventTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'Events'])
    class Meta:
        model = Events
        order_by='Date'
        attrs = {"class": "table table-bordered"}
