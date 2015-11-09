from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from django.template import RequestContext, loader
# Create your views here.

def index(request):
	player_list = Player.objects.all()
	template = loader.get_template('tracker/index.html')
	context = RequestContext(request, {
		'player_list': player_list,
	})
	
	return HttpResponse(template.render(context))
	
def player(request, player_id):
	response = "Player: %s"
	return HttpResponse(response % player_id)

