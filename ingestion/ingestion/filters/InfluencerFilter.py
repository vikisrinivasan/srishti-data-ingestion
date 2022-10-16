import django_filters

from ..models.Influencers import  Influencers


class InfluencerFilter(django_filters.FilterSet):
    class Meta:
        model =  Influencers
        fields = ['Name']