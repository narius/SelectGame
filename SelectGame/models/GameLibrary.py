from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User

from .Game import Game

# Create your models here.


class GameLibrary(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    games = models.ManyToManyField(Game, verbose_name=gettext("games"))

    class Meta:
        verbose_name = gettext("game library")
        verbose_name_plural = gettext("game library")

    def __str__(self):
        return gettext("library")+" "+str(self.owner)
