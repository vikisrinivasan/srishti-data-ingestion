import django_filters

from ..models.PhotographerLeads import PhotographerLeads


class PhotographerLeadsFilter(django_filters.FilterSet):
    class Meta:
        model =  PhotographerLeads
        fields = ['Name']