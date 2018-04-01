from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from .Event import Event
from .Rating import Rating
from .Game import Game


class EventGame(models.Model):
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='games')
    games = models.ManyToManyField(Rating)


class EventGameVote(models.Model):
    event_game = models.ForeignKey(EventGame,
                                   on_delete=models.CASCADE,
                                   related_name='votes')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,)
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,)

    class Meta:
        verbose_name = gettext('event game vote')
        verbose_name_plural = gettext('event game votes')
        unique_together = ('game', 'user')

    def __str__(self):
        return str(self.event_game)+" - "+str(self.user)
