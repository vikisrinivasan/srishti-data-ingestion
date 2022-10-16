import django_filters

from ..models.EventRegistration import EventRegistration


class EventRegistrationFilter(django_filters.FilterSet):
    class Meta:
        model =  EventRegistration
        fields = ['Name']