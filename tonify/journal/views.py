# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import json
import commands
import unirest
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def analyzeTone(request):
    if (request.method == 'POST'):
        text = request.POST['input']
        url = "https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze"
        params = {"version": "2017-02-27", "text" : text, "features" : "emotion"}
        auth = ("96218d67-7e51-44e3-911f-f96e0c14570b", "rj86GIfAotc0")
        res = unirest.post(url, params=params, auth=auth)
        return JsonResponse(json.loads(res.body))
    else:
        return HttpResponse("Incorrect http method", status=405);
