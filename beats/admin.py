from django.contrib import admin
from .models import Artist, Beat

class BeatInline(admin.TabularInline):
    model = Beat.artist.through
    extra = 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [BeatInline]

@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    #list_display = ('name', 'bpm', 'display_artist')
    list_filter = ('artist', 'bpm')
    #fieldsets = (
    #    (None, {
    #        'fields': ('name', 'bpm', 'wrap', 'display_artist')
    #    }),
    #    ('Audio', {
    #        'fields': ('wave', 'mp3')
    #    }),
    #)

