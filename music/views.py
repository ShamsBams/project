from django.shortcuts import render
from .models import Genre, Music, Musician

def index(request):
    genre = Genre.objects.all()
    musician = Musician.objects.all()
    music = Music.objects.all()
    context = {
        'genre': genre,
        'music': music,
        'musician': musician,

    }
    return render(request, 'music/index.html', context)