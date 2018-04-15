from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
# Create your models here.

NOTIFICATION_STATUS_UNREAD = 'UR'
NOTIFICATION_STATUS_READ = 'RE'
STATUS = (
        (NOTIFICATION_STATUS_UNREAD, gettext("Unread")),
        (NOTIFICATION_STATUS_READ, gettext("Read")),
    )


class Notification(models.Model):

    status = models.CharField(max_length=2, choices=STATUS, default="UR")
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="notification_sender",
                               verbose_name=gettext("sender"))
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="notification_receiver",
                                 verbose_name=gettext("receiver"))

    class Meta:
        verbose_name = gettext("notification")
        verbose_name_plural = gettext("notifications")

    def __str__(self):
        return str(self.sender)+" - "+str(self.receiver)+" - "+self.status
