import django_tables2 as tables
from django_tables2 import TemplateColumn
from django_tables2.utils import A
from ..models.SocialMediaEnquiries import SocialMediaEnquiries

# Create the form class.
class SocialMediaEnquiriesTable(tables.Table):
    delete = tables.LinkColumn('delete_item', text='Delete',args=[A('pk'),'SocialMediaEnquiries'])
    class Meta:
        model = SocialMediaEnquiries
        order_by='ReceivedDate'
        attrs = {"class": "table table-bordered"}
