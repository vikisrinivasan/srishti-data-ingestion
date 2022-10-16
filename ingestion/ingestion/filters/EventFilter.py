import django_filters

from ..models.Events import Events


class EventFilter(django_filters.FilterSet):
    class Meta:
        model =  Events
        fields = ['Name']


