# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import ServiceTable


# Registered the service table model.
admin.site.register(ServiceTable)