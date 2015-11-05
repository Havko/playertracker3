from django.db import models

# Create your models here.

class Player(models.Model):
	touchdowns = models.IntegerField(default=0)