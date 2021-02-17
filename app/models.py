# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceTable(models.Model): 
    date = models.CharField(default='', max_length=255)
    service = models.CharField(default='', max_length=255) 
    environment = models.IntegerField(default = 0)
    annotation = models.CharField(default='', max_length=255)




    