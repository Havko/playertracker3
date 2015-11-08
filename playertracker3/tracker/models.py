from django.db import models

# Create your models here.

class Player(models.Model):
	player_name = models.CharField(max_length=200, default = 'default_value')
	touchdowns = models.IntegerField(default=0)
	def __unicode__(self):
		return self.player_name