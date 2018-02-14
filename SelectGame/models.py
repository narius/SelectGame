from django.db import models
from django.utils.translation import gettext
from  django.contrib.auth.models import User
# Create your models here.

#Model for categories
class model_category(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name="Name")
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

#Model for games
class model_game(models.Model):
    name=models.CharField(max_length=30, verbose_name="Name")
    category=models.ManyToManyField(model_category)
    comment=models.TextField(verbose_name="Comment")
    class Meta:
        verbose_name = gettext("game")
        verbose_name_plural = gettext("games")
    def __str__(self):
        return self.name
#toppings = models.ManyToManyField(Topping)

#Model for ratings

#Model for location
class model_location(models.Model):
    address=models.CharField(max_length=100, verbose_name=gettext("address"))
    owner = models.ForeignKey(User)
    class Meta:
        verbose_name=gettext("Address")
        verbose_name_plural=gettext("Address")
    def __str__(self):
        return self.owner+"-"+self.address
