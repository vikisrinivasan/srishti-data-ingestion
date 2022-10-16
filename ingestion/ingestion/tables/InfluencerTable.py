import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.Influencers import  Influencers

# Create the form class.
class InfluencerTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'Influencers'])
    class Meta:
        model = Influencers
        order_by='Date'
        attrs = {"class": "table table-bordered"}
