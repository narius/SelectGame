from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class model_group(models.Model):
    name=models.CharField(max_length=30, verbose_name=gettext('name'))
    owners=models.ManyToManyField(User,verbose_name=gettext('owners'), related_name="group_owner")
    members=models.ManyToManyField(User, verbose_name=gettext('members'), related_name="group_members")
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
    biography=models.TextField(verbose_name=gettext('biography'), null=True, blank=True)
    avatar=models.ImageField(null=True,upload_to='uploads/avatars', blank=True)
    class Meta:
        verbose_name=gettext('user profile')
        verbose_name_plural=gettext('user profiles')
    def __str__(self):
        return str(self.user)

#Status for friends
friends_pending='pe'
friends_accepted='ac'
friends_rejected='re'
friends_removed='rm'
FRIENDS_STATUS=(
    (friends_pending,gettext('pending approval')),
    (friends_accepted,gettext('accepted')),
    (friends_rejected,gettext('rejected')),
    (friends_removed,gettext('removed')),
)
class model_friends(models.Model):
    status_user1=models.CharField(max_length=2,choices=FRIENDS_STATUS,default=friends_pending)
    status_user2=models.CharField(max_length=2,choices=FRIENDS_STATUS,default=friends_pending)
    user1=models.ForeignKey(User, related_name="User1", on_delete=models.CASCADE)
    user2=models.ForeignKey(User, related_name="User2", on_delete=models.CASCADE)
    class Meta:
        verbose_name=gettext("friend")
        verbose_name_plural=gettext("friends")
        unique_together = (("user1", "user2"),)
    def __str__(self):
        return str(self.user1)+"("+self.get_status_user1_display()+") - "+str(self.user2)+"("+self.get_status_user2_display()+")"

class model_private_message(models.Model):
    participants=models.ManyToManyField(User, verbose_name=gettext('participants'), related_name="participants")
    messages=models.ManyToManyField(model_message)
    class Meta:
        verbose_name=gettext("private message")
        verbose_name_plural=gettext("private messages")
    def __str__(self):
        return str(self.participants)
