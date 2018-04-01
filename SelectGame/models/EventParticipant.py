from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext

from .Event import Event

EVENT_STATUS_WILL_COME = 'WC'
EVENT_STATUS_MAYBE = 'MA'
EVENT_STATUS_NOT_COMING = 'NC'
EVENT_STATUS_PENDING = 'PE'

EVENT_ROLES_OWNER = 'OW'
EVENT_ROLES_PARTICIPANT = 'PA'

STATUS = (
    (EVENT_STATUS_WILL_COME, gettext("Will come")),
    (EVENT_STATUS_MAYBE, gettext("Maybe")),
    (EVENT_STATUS_NOT_COMING, gettext("Not coming")),
    (EVENT_STATUS_PENDING, gettext("Pending"))
)
ROLES = (
    (EVENT_ROLES_OWNER, gettext("Owner")),
    (EVENT_ROLES_PARTICIPANT, gettext("Participant"))
)

GLYPHICONS = {
    EVENT_STATUS_WILL_COME: 'material-icons event_status_will_come',
    EVENT_STATUS_MAYBE: 'material-icons event_status_maybe',
    EVENT_STATUS_NOT_COMING: 'material-icons event_status_not_coming',
    EVENT_STATUS_PENDING: 'material-icons event_status_pending',
}


class EventParticipant(models.Model):
    '''
        An event participant is a user that might take part in an event
    '''
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="event_participant")
    status = models.CharField(max_length=2, choices=STATUS, default="PE")
    role = models.CharField(max_length=2, choices=ROLES, default="PA")
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name="participants")
    glyphicon = models.CharField(max_length=100,
                                 default="material-icons event_status_pending'")

    class Meta:
        verbose_name = gettext("event participant")
        verbose_name_plural = gettext("event participants")
        unique_together = ("user", "event")

    def save(self, *args, **kwargs):
        self.glyphicon = GLYPHICONS[self.status]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.event.name+" - "+str(self.user)
