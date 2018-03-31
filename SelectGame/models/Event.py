from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Model from SelectGame
from .Game import Game
from .Location import Location

# Models from Social
from Social.models import Group
from Social.models import UserMessage
from Social.models import Notification
# Create your models here.


class Event(models.Model):
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="event_creator")
    date = models.DateTimeField(verbose_name=gettext("date"))
    games = models.ManyToManyField(Game,
                                   verbose_name=gettext("games"),
                                   blank=True)
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 verbose_name=gettext("location"))
    is_public = models.BooleanField(verbose_name=gettext("public"))
    group = models.ForeignKey(Group,
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True)
    name = models.CharField(max_length=100,
                            verbose_name=gettext("name"),
                            blank=True)
    messages = models.ManyToManyField(UserMessage, blank=True)
    minimum_number_of_players = models.IntegerField(default=1,
                                                    verbose_name=gettext("minimum number of players"),
                                                    validators=[MinValueValidator(1)])
    maximum_number_of_players = models.IntegerField(default=1,
                                                    verbose_name=
                                                    gettext("maximum number of players"),
                                                    validators=[
                                                        MaxValueValidator(100)])
    notifications = models.ManyToManyField(Notification,
                                           related_name='event')

    class Meta:
        verbose_name = gettext("event")
        verbose_name_plural = gettext("events")

    def __str__(self):
        return str(self.creator)+" "+str(self.date)
