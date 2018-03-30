from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from .Game import Game
# Create your models here.


class Rating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name=gettext("rating"),
                                 default=0,
                                 validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])
    review = models.TextField(verbose_name=gettext("review"), blank=True)

    class Meta:
        verbose_name = gettext("rating")
        verbose_name_plural = gettext("ratings")
        # A user may only rate a game once
        unique_together = (("game", "user"),)

    def __str__(self):
        return str(self.user)+" "+str(self.game)+" "+str(self.rating)
