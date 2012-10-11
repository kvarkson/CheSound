from models import Chord
from django.http import HttpResponseRedirect, HttpResponse
#import datetime, calendar, string, urllib2, os, shutil
#from xml.dom.minidom import parseString
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def index(request):
    chords = Chord.objects.all()
    return render_to_response('base.html', {'chords': chords,})
