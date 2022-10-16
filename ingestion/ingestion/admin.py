# -*- coding: utf-8 -*-
from django.contrib import admin

from django.apps import apps
from .models.PhotographerLeads import PhotographerLeads
from .models.EventRegistration import EventRegistration
from .models.Events import Events
from .models.Influencers import Influencers
from .models.InstitutionalClients import InstitutionalClients
from .models.ServiceRequest import ServiceRequests
from .models.SocialMediaEnquiries import SocialMediaEnquiries

models = apps.get_models()



@admin.register(PhotographerLeads,EventRegistration,Events,Influencers,InstitutionalClients,
                ServiceRequests,SocialMediaEnquiries)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

