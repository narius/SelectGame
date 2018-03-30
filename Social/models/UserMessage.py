from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from .Notification import Notification
# Create your models here.


class UserMessage(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=gettext('text'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=gettext('created'))
    notification = models.ForeignKey(Notification,
                                     related_name='message',
                                     null=True,
                                     on_delete=models.CASCADE,
                                     verbose_name=gettext("notification"))

    class Meta:
        verbose_name = gettext('message')
        verbose_name_plural = gettext('messages')
        ordering = ['-created_date']

    def __str__(self):
        return str(self.created_date)+": "+self.text
