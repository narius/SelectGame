from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

#Models from Social
from Social.models import model_group
# Create your models here.

#Model for categories
class model_category(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name=gettext("name"))
    class Meta:
        verbose_name = gettext("category")
        verbose_name_plural = gettext("categories")
    def __str__(self):
        return self.name

#Model for games
class model_game(models.Model):
    name=models.CharField(max_length=30, verbose_name=gettext("name"))
    category=models.ManyToManyField(model_category)
    comment=models.TextField(verbose_name=gettext("Comment"), blank=True)
    class Meta:
        verbose_name = gettext("game")
        verbose_name_plural = gettext("games")
    def __str__(self):
        return self.name

#Model for ratings
class model_rating(models.Model):
    game=models.ForeignKey(model_game, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(verbose_name=gettext("rating"),
            default=0,
            validators=[MaxValueValidator(5), MinValueValidator(0)])
    review=models.TextField(verbose_name=gettext("review"), blank=True)
    class Meta:
        verbose_name=gettext("rating")
        verbose_name_plural=gettext("ratings")
    def __str__(self):
        return str(self.user)+" "+str(self.game)+" "+str(self.rating)

#Model for location
class model_location(models.Model):
    address=models.CharField(max_length=100, verbose_name=gettext("address"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name=gettext("Address")
        verbose_name_plural=gettext("Address")
    def __str__(self):
        return str(self.owner)+"-"+str(self.address)

#Model for an event.
class model_event(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_owner")
    participants=models.ManyToManyField(User, verbose_name=gettext("participants"), related_name="event_participants")
    date=models.DateTimeField(verbose_name=gettext("date"))
    games=models.ManyToManyField(model_game, verbose_name=gettext("games"))
    location=models.ForeignKey(model_location, on_delete=models.CASCADE, verbose_name=gettext("location"))
    is_public=models.BooleanField(verbose_name=gettext("public"))
    group=models.ForeignKey(model_group, blank=True, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name=gettext("event")
        verbose_name_plural=gettext("events")
    def __str__(self):
        return str(self.owner)+" "+str(self.date)

#A model for games that a person owns
class model_game_library(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_owner")
    games=models.ManyToManyField(model_game, verbose_name=gettext("games"))
    class Meta:
        verbose_name=gettext("game library")
        verbose_name_plural=gettext("game library")
    def __str__(self):
        return gettext("library")+" "+str(self.owner)
