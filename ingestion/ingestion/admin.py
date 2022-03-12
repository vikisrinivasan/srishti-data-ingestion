# -*- coding: utf-8 -*-
from django.contrib import admin

from django.apps import apps
from .models.leads import Leads
from .models.contacts import Contacts
models = apps.get_models()

for model in [Leads,Contacts]:
    admin.site.register(model)
