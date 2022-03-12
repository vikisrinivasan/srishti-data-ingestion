import django_tables2 as tables
from .models.leads import Leads

class LeadsTable(tables.Table):
    class Meta:
        model = Leads
        template_name = "django_tables2/bootstrap.html"