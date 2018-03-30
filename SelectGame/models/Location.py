from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    address = models.CharField(max_length=100, verbose_name=gettext("address"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = gettext("Address")
        verbose_name_plural = gettext("Address")

    def __str__(self):
        return str(self.owner)+"-"+str(self.address)
