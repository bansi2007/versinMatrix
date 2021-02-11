# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import json


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

# This the json data that has to be accessed.
def version_matrix(request):
    print(request.GET)
    data =  [  {"date":"10-11-2020","service":"service_abc", "environment":"1.0", "annotation":"OK"},
    {"date":"10-11-2020","service":"service_vwx", "environment":"1.0", "annotation":"VersionMismatch"},
    {"date":"10-11-2020","service":"service_xyz", "environment":"1.2", "annotation":"VersionMismatch"},
    {"date":"10-12-2020","service":"service_yz", "environment":"1.6", "annotation":"OK"},
    {"date":"10-11-2020","service":"service_def", "environment":"1.9", "annotation":"VersionMismatch"},
    {"date":"10-11-2020","service":"service_123", "environment":"1.0", "annotation":"OK"},
    {"date":"10-16-2020","service":"service_ghi", "environment":"1.6", "annotation":"OK"},
    {"date":"10-16-2020","service":"service_456", "environment":"1.4", "annotation":"VersionMismatch"},
    {"date":"10-16-2020","service":"service_789", "environment":"1.8", "annotation":"OK"},
    {"date":"10-11-2020","service":"service_ABC", "environment":"1.0", "annotation":"OK"},
    {"date":"10-11-2020","service":"service_DEF", "environment":"2.6", "annotation":"OK"},
    {"date":"10-16-2020","service":"service_GHI", "environment":"1.6", "annotation":"VersionMismatch"},
    {"date":"10-16-2020","service":"service_JKL", "environment":"2.0", "annotation":"OK"},
    {"date":"10-09-2020","service":"service_jkl", "environment":"1.2", "annotation":"OK"},
    {"date":"10-09-2020","service":"service_mno", "environment":"1.8", "annotation":"VersionMismatch"},
    {"date":"10-09-2020","service":"service_pqr", "environment":"1.6", "annotation":"OK"},
    {"date":"10-09-2020","service":"service_stu", "environment":"17", "annotation":"OK"}
 ]
    return HttpResponse(json.dumps({'data':data}), content_type = 'applications/json')