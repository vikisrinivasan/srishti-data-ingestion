import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..filters.EventRegistrationFilter import EventRegistrationFilter
from ..models.EventRegistration import EventRegistration

# Create the form class.
class EventRegistrationTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'EventRegistration'])
    class Meta:
        model = EventRegistration
        order_by='id'
        attrs = {"class": "table table-bordered"}
