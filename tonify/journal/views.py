# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import json
import commands
import unirest
import requests
import operator
# Create your views here.

def index(request):
   return render(request, 'index.html', {})

def getAuthToken():
   params = {"grant_type" : "client_credentials"}
   headers = {"Authorization": "Basic OGVjNWE2N2RhNGExNDg4NWIwZWY4YWJkZDAyMDhlNDk6NTgwZGY0MzI4NmE3NGJjYjk1MDExNjVkYjQzN2IzZTc="}
   res = unirest.post("https://accounts.spotify.com/api/token", params=params, headers=headers)
   return res.body['access_token']

def returnPlaylist(request):
   if (request.method == 'POST'):
      text = request.POST['input']
      auth_token = getAuthToken()
      sentiment_values = analyzeTone(text)
      playlist = generatePlaylist(sentiment_values, auth_token)
      return JsonResponse(playlist)
   else:
      return HttpResponse("Incorrect http method", status=405);

def analyzeTone(text):
   url = "https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze"
   params = {"version": "2017-02-27", "text" : text, "features" : "emotion"}
   auth = ("96218d67-7e51-44e3-911f-f96e0c14570b", "rj86GIfAotc0")
   res = unirest.get(url, params=params, auth=auth)
   print res.body # <-------------

   return res.body["emotion"]["document"]["emotion"]

def top_emotion(sentiment_values):
   emotion = max(sentiment_values.iteritems(), key=operator.itemgetter(1))[0]
   return emotion

def artist_seed(emotion):
   seed = "3wyVrVrFCkukjdVIdirGVY"
   if emotion == "anger":
      seed = "7dGJo4pcD2V6oG8kP0tJRR"
   elif emotion == "fear":
      seed = "26bcq2nyj5GB7uRr558iQg"
   elif emotion == "joy":
      seed = "5YGY8feqx7naU7z4HrwZM6"
   elif emotion == "sadness":
      seed = "3TVXtAsR1Inumwj472S9r4"
   return seed


def song_seed(emotion):
   seed = "43ZyHQITOjhciSUUNPVRHc"
   if emotion == "anger":
      seed = "6PPRKnwToRK9GjTCV03vlG"
   elif emotion == "fear":
      seed = "2KH16WveTQWT6KOG9Rg6e2"
   elif emotion == "joy":
      seed = "5Q0Nhxo0l2bP3pNjpGJwV1"
   elif emotion == "sadness":
      seed = "2z3htsNRuhDN923ITatc56"
   return seed

def generatePlaylist(sentiment_values, auth_token):
   valence = sentiment_values["joy"]
   top = top_emotion(sentiment_values)
   seed_artist = artist_seed(top_emotion)
   seed_song = song_seed(top_emotion)

   url = "https://api.spotify.com/v1/recommendations"
   params = {"min_energy" : valence,"max_mode" : "5", "market" : "US", "min_danceability" : valence, "seed_tracks" : seed_song , "seed_artists" : seed_artist , "target_popularity" : "30", "min_valence" : valence, }
   headers = {"Authorization": "Bearer " + auth_token}

   res = unirest.get(url, headers=headers, params=params)
   print res.body
   return res.body
