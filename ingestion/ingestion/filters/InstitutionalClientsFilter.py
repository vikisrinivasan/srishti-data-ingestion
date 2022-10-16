import django_filters

from ..models.InstitutionalClients import InstitutionalClients


class InstitutionalClientsFilter(django_filters.FilterSet):
    class Meta:
        model =  InstitutionalClients
        fields = ['Name']