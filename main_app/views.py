from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Song:
  def __init__(self, title, artist, memory):
    self.title = title
    self.artist = artist
    self.memory = memory

songs = [
  Song('Sweater Weather', 'The Neighbourhood', 'Listened to it the first time driving the high school')
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  return render(request, 'songs/index.html', {'songs': songs})