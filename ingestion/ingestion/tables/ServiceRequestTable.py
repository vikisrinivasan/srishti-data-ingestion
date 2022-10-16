import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.ServiceRequest import ServiceRequests

# Create the form class.
class ServiceRequestTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'ServiceRequests'])
    class Meta:
        model = ServiceRequests
        order_by='RequestID'
        attrs = {"class": "table table-bordered"}
