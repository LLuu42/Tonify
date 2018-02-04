# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', {})
