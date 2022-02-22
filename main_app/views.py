from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Song

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST) 
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index') 
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def songs_index(request):
  songs = Song.filter(user=request.user)
  return render(request, 'songs/index.html', {'songs': songs})

@login_required
def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  return render(request, 'songs/detail.html', {'song': song})

class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  fields = ('title', 'artist', 'memory')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SongUpdate(LoginRequiredMixin, UpdateView):
  model = Song
  fields = ('title', 'artist', 'memory')

class SongDelete(LoginRequiredMixin, DeleteView):
  model = Song
  success_url = '/songs/'
 