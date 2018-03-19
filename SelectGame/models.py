from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

#Models from Social
from Social.models import Group
from Social.models import UserMessage
# Create your models here.

#Model for categories
class Category(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name=gettext("name"))
    class Meta:
        verbose_name = gettext("category")
        verbose_name_plural = gettext("categories")
        ordering = ['name']
    def __str__(self):
        return self.name

#Model for games
class Game(models.Model):
    image=models.ImageField(null=True,upload_to='uploads/game_images', blank=True)
    name=models.CharField(max_length=30, verbose_name=gettext("name"))
    category=models.ManyToManyField(Category)
    comment=models.TextField(verbose_name=gettext("Comment"), blank=True)
    minimum_number_of_players=models.IntegerField(default=1,
                        verbose_name=gettext("minimum number of players"),
                        validators=[MinValueValidator(1)])
    maximum_number_of_players=models.IntegerField(default=1,
                        verbose_name=gettext("maximum number of players"),
                        validators=[MaxValueValidator(100)])
    link = models.URLField(max_length=200, verbose_name=gettext("link"), blank=True)
    class Meta:
        verbose_name = gettext("game")
        verbose_name_plural = gettext("games")
        ordering = ["name"]
    def __str__(self):
        return self.name

#Model for ratings
class Rating(models.Model):
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(verbose_name=gettext("rating"),
            default=0,
            validators=[MaxValueValidator(5), MinValueValidator(0)])
    review=models.TextField(verbose_name=gettext("review"), blank=True)
    class Meta:
        verbose_name=gettext("rating")
        verbose_name_plural=gettext("ratings")
        #A user may only rate a game once
        unique_together = (("game", "user"),)
    def __str__(self):
        return str(self.user)+" "+str(self.game)+" "+str(self.rating)

#Model for location
class Location(models.Model):
    address=models.CharField(max_length=100, verbose_name=gettext("address"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name=gettext("Address")
        verbose_name_plural=gettext("Address")
    def __str__(self):
        return str(self.owner)+"-"+str(self.address)

#Model for an event.
class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_owner")
    participants = models.ManyToManyField(User, verbose_name=gettext("participants"), related_name="event_participants", blank=True)
    date = models.DateTimeField(verbose_name=gettext("date"))
    games = models.ManyToManyField(Game, verbose_name=gettext("games"), blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=gettext("location"))
    is_public = models.BooleanField(verbose_name=gettext("public"))
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name=gettext("name"), blank=True)
    messages = models.ManyToManyField(UserMessage, blank=True)
    minimum_number_of_players = models.IntegerField(default=1,
                    verbose_name=gettext("minimum number of players"),
                    validators=[MinValueValidator(1)])
    maximum_number_of_players = models.IntegerField(default=1,
                    verbose_name=gettext("maximum number of players"),
                    validators=[MaxValueValidator(100)])
    class Meta:
        verbose_name = gettext("event")
        verbose_name_plural = gettext("events")
    def __str__(self):
        return str(self.owner)+" "+str(self.date)

#A model for games that a person owns
class  GameLibrary(models.Model):
    owner=models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    games=models.ManyToManyField(Game, verbose_name=gettext("games"))
    class Meta:
        verbose_name=gettext("game library")
        verbose_name_plural=gettext("game library")
    def __str__(self):
        return gettext("library")+" "+str(self.owner)
