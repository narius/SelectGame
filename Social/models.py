from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
# Create your models here.
class model_group(models.Model):
    name=models.CharField(max_length=30, verbose_name=gettext('name'))
    owners=models.ManyToManyField(User,verbose_name=gettext('owners'), related_name="group_owner")
    members=models.ManyToManyField(User, verbose_name=gettext('participants'), related_name="group_members")
    class Meta:
        verbose_name=gettext('group')
        verbose_name_plural=gettext('groups')
    def __str__(self):
        return self.name

class model_message(models.Model):
    text=models.TextField(verbose_name=gettext('text'))
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=gettext('created'))
    class Meta:
        verbose_name=gettext('message')
        verbose_name_plural=gettext('messages')
    def __str__(self):
        return str(self.created_date)+": "+self.text

class model_group_message(models.Model):
    group=models.ForeignKey(model_group, on_delete=models.CASCADE)
    messages=models.ManyToManyField(model_message)
    class Meta:
        verbose_name=gettext('group message')
        verbose_name_plural=gettext('group messages')
    def __str__(self):
        return 'Group message'+str(self.group)

class model_user_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    biography=models.TextField(verbose_name=gettext('biography'))
    class Meta:
        verbose_name=gettext('user profile')
        verbose_name_plural=gettext('user profiles')
    def __str__(self):
        return str(self.user)


#TODO: model for friends

#TODO: model for friend requests

#TODO: model for private messages
