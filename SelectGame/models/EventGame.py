from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext

from .Event import Event
from .Game import Game


class EventGame(models.Model):
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='games')
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE)
    average = models.FloatField(default=0)
    number_of_rated = models.IntegerField(default=0)
    too_low = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event)+" - "+str(self.game)


class EventGameVote(models.Model):
    event_game = models.ForeignKey(EventGame,
                                   on_delete=models.CASCADE,
                                   related_name='votes')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,)

    class Meta:
        verbose_name = gettext('event game vote')
        verbose_name_plural = gettext('event game votes')
        unique_together = ('event_game', 'user')

    def __str__(self):
        return str(self.event_game)+" - "+str(self.user)
