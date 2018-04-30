from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

NOTIFICATION_STATUS_UNREAD = 'UR'
NOTIFICATION_STATUS_READ = 'RE'
STATUS = (
        (NOTIFICATION_STATUS_UNREAD, gettext("Unread")),
        (NOTIFICATION_STATUS_READ, gettext("Read")),
    )


class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default="UR")
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="notification_sender",
                               verbose_name=gettext("sender"))
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="notification_receiver",
                                 verbose_name=gettext("receiver"))

    @property
    def link(self):
        #Returns link to group
        if self.group.all().count()>0:
            return
        elif self.message.all().count()>0:
            return reverse('social:view_messages')
        elif self.event.all().count()>0:
            event = self.event.all().first()
            return reverse('social:view_event', kwargs={'event_id':event.id})

    class Meta:
        verbose_name = gettext("notification")
        verbose_name_plural = gettext("notifications")
        ordering = ['-created']

    def __str__(self):
        return str(self.sender)+" - "+str(self.receiver)+" - "+self.status
