from django.db import models
from django.utils.translation import gettext
from Social.models import Group
from Social.models import UserMessage
# Create your models here.


class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    messages = models.ManyToManyField(UserMessage)

    class Meta:
        verbose_name = gettext('group message')
        verbose_name_plural = gettext('group messages')

    def __str__(self):
        return 'Group message'+str(self.group)
