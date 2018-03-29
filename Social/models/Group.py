from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from .UserMessage import UserMessage
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name=gettext('name'))
    owners = models.ManyToManyField(User,
                                    verbose_name=gettext('owners'),
                                    related_name="group_owner")
    members = models.ManyToManyField(User,
                                     verbose_name=gettext('members'),
                                     related_name="group_members")

    messages = models.ManyToManyField(UserMessage,
                                      verbose_name=gettext("messages"))

    class Meta:
        verbose_name = gettext('group')
        verbose_name_plural = gettext('groups')

    def __str__(self):
        return self.name
