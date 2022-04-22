from django.shortcuts import render
from beatstore.settings import YOUTUBE_API_KEY
from .models import Beat, Artist
from django.views.generic import ListView


beats_list = Beat.objects.all()

class ArtistSearch:
    def get_artists(self):
        return Artist.objects.all()

class BeatsListView(ArtistSearch, ListView):
    paginate_by = 15
    model = Beat
    def get_queryset(self):
        kwargs = {}
        if self.request.GET.get('artist'):
            kwargs["artist__in"] = self.request.GET.getlist('artist')
        if self.request.GET.get('bpm'):
            kwargs["bpm"] = self.request.GET.get('bpm')
        if self.request.GET.get('nm'):
            kwargs["name__icontains"] = self.request.GET.get('nm')
        return Beat.objects.filter(**kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['artist'] = self.request.GET.get('artist')
        context['bpm'] = self.request.GET.get('bpm')
        context['nm'] = self.request.GET.get('nm')
        return context

def index(request):
    beat_list = beats_list[:2]

    return render(request, 'index_major.html', context={'beat_list':beat_list, 'youtube_api_key' : YOUTUBE_API_KEY})

def terms(request):
    beat_list = beats_list[:2]

    return render(request, 'terms_major.html', context={'beat_list':beat_list,})



