import django_filters

from ..models.SocialMediaEnquiries import SocialMediaEnquiries


class SocialMediaEnquiriesFilter(django_filters.FilterSet):
    class Meta:
        model = SocialMediaEnquiries
        fields = ['Name']