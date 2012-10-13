from django.db.models.fields.related import ForeignKey
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

SOUND_CHOICES = (
    ('1A', '1A'),
    ('1As', '1As'),
    ('1B', '1B'),
    ('2C', '2C'),
    ('2Cs', '2Cs'),
    ('2D', '2D'),
    ('2Ds', '2Ds'),
    ('2E', '2E'),
    ('2F', '2F'),
    ('2Fs', '2Fs'),
    ('2G', '2G'),
    ('2Gs', '2Gs'),
    ('2A', '2A'),
    ('2As', '2As'),
    ('2B', '2B'),
    ('3C', '3C'),
    ('3Cs', '3Cs'),
    ('3D', '3D'),
    ('3Ds', '3Ds'),
    ('3E', '3E'),
    ('3F', '3F'),
    ('3Fs', '3Fs'),
    ('3G', '3G'),
    ('3Gs', '3Gs'),
    ('3A', '3A'),
    ('3As', '3As'),
    ('3B', '3B'),
    ('4C', '4C'),
)

# Model class for chords
class Chord(models.Model):
    name = models.CharField(max_length=50)
    root = models.CharField(max_length=3, choices=SOUND_CHOICES, default='')
    first = models.CharField(max_length=3, choices=SOUND_CHOICES, default='')
    second = models.CharField(max_length=3, choices=SOUND_CHOICES, default='')
    third = models.CharField(max_length=3, choices=SOUND_CHOICES, default='')
    
    def __unicode__(self):
        return self.name

admin.site.register(Chord)