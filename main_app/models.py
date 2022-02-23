from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    memory = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': self.id})