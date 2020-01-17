from django.shortcuts import render
from players.models import Player
# Create your views here.

def homeview(request):
    players = Player.objects.all()
    context= {
        'players':players
    }
    return render(request, 'home.html', context)