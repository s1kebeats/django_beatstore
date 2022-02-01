from django import forms
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Beat(models.Model):
    name = models.CharField(max_length=50, help_text='Type beat name.')
    bpm = models.SmallIntegerField(help_text='Type BPM for the beat.')
    artist = models.ManyToManyField(Artist, help_text='Select Artists for the beat')
    wrap = models.ImageField(upload_to='wraps/', default='images/wraps/S.svg')
    wave = models.FileField(upload_to='audio/wave/', default='')
    mp3 = models.FileField(upload_to='audio/mp3/', default='')
    def __str__(self):
        return self.name
    def display_artist(self):
        return ', '.join([artist.name for artist in self.artist.all()])
    display_artist.short_description = 'Artist'