from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    STATUS = (
        ('UR', gettext("Unread")),
        ('RE', gettext("Read")),
    )
    status = models.CharField(max_length=2, choices=STATUS, default="UR")
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="not_sender",
                               verbose_name=gettext("sender"))
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="not_receiver",
                                 verbose_name=gettext("receiver"))

    class Meta:
        verbose_name = gettext("notification")
        verbose_name_plural = gettext("notifications")

    def __str__(self):
        return str(self.sender)+" - "+str(self.receiver)+" - "+self.status
