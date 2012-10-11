from django.db.models.fields.related import ForeignKey
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Model class for chords
class Chord(models.Model):
    name = models.CharField(max_length=50)
    c = models.BooleanField()
    c_sharp = models.BooleanField()
    d = models.BooleanField()
    d_sharp = models.BooleanField()
    e = models.BooleanField()
    e_sharp = models.BooleanField()
    f = models.BooleanField()
    f_sharp = models.BooleanField()
    g = models.BooleanField()
    g_sharp = models.BooleanField()
    a = models.BooleanField()
    a_sharp = models.BooleanField()
    b = models.BooleanField()
    
    def __unicode__(self):
        return self.name

admin.site.register(Chord)