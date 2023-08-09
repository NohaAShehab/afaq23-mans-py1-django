from django.shortcuts import render

# Create your views here.
from tracks.models import Track

def index(request):
    # get tracks from the database
    # tracks = Track.objects.all()
    tracks = Track.get_all_tracks()
    return  render(request, 'tracks/index.html', context={'tracks':tracks})
