from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext

from .Category import Category

# Create your models here.


class Game(models.Model):
    image = models.ImageField(null=True,
                              upload_to='uploads/game_images',
                              blank=True)
    name = models.CharField(max_length=30, verbose_name=gettext("name"))
    category = models.ManyToManyField(Category)
    comment = models.TextField(verbose_name=gettext("Comment"), blank=True)
    minimum_number_of_players = models.IntegerField(default=1,
                        verbose_name=gettext("minimum number of players"),
                        validators=[MinValueValidator(1)])
    maximum_number_of_players = models.IntegerField(default=1,
                        verbose_name=gettext("maximum number of players"),
                        validators=[MaxValueValidator(100)])
    link = models.URLField(max_length=200,
                           verbose_name=gettext("link"),
                           blank=True)

    class Meta:
        verbose_name = gettext("game")
        verbose_name_plural = gettext("games")
        ordering = ["name"]

    def __str__(self):
        return self.name
