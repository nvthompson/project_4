from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Song

# Create your views here.
# class Song:
#   def __init__(self, title, artist, memory):
#     self.title = title
#     self.artist = artist
#     self.memory = memory

# songs = [
#   Song('Sweater Weather', 'The Neighbourhood', 'Listened to it the first time driving the high school')
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  songs = Song.objects.all()
  return render(request, 'songs/index.html', {'songs': songs})

def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  return render(request, 'songs/detail.html', {'song': song})

class SongCreate(CreateView):
  model = Song
  fields = ('title', 'artist', 'memory')
 