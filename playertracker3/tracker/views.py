from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

# Create your views here.

def index(request):
	player_list = Player.objects.all()
	
	context =  {	'player_list': player_list}
	
	return render(request, 'tracker/index.html', context)
	
def player(request, player_id):
	response = "Player: %s"
	return HttpResponse(response % player_id)

