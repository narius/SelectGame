from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from Social.models import UserMessage
from Social.models import Notification
# Create your models here.


class PrivateMessage(models.Model):
    participants = models.ManyToManyField(User,
                                          verbose_name=gettext('participants'),
                                          related_name="participants")
    messages = models.ManyToManyField(UserMessage)
    notification = models.ManyToManyField(Notification,
                                     related_name='message',
                                     null=True,
                                     blank=True,
                                     verbose_name=gettext("notification"))
    class Meta:
        verbose_name = gettext("private message")
        verbose_name_plural = gettext("private messages")

    def __str__(self):
        return str(self.participants)
