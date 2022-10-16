import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.PhotographerLeads import  PhotographerLeads

# Create the form class.
class PhotographerLeadsTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'PhotographerLeads'])
    class Meta:
        model = PhotographerLeads
        order_by='lead_created_date'
        attrs = {"class": "table table-bordered"}
