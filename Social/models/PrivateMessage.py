from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from Social.models import UserMessage
# Create your models here.


class PrivateMessage(models.Model):
    participants = models.ManyToManyField(User,
                                          verbose_name=gettext('participants'),
                                          related_name="participants")
    messages = models.ManyToManyField(UserMessage)

    class Meta:
        verbose_name = gettext("private message")
        verbose_name_plural = gettext("private messages")

    def __str__(self):
        return str(self.participants)
