from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from .models import Player

# Create your views here.

def index(request):
	player_list = Player.objects.all()
	
	context =  {	'player_list': player_list}
	
	return render(request, 'tracker/index.html', context)
	
def player(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	return render(request, 'tracker/player.html', {'player': player})

