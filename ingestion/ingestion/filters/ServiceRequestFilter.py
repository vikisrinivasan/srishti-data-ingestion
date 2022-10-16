import django_filters

from ..models.ServiceRequest import ServiceRequests


class ServiceRequestFilter(django_filters.FilterSet):
    class Meta:
        model =  ServiceRequests
        fields = ['Name']