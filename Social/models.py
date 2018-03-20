from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name=gettext('name'))
    owners = models.ManyToManyField(User,
                                    verbose_name=gettext('owners'),
                                    related_name="group_owner")
    members = models.ManyToManyField(User,
                                     verbose_name=gettext('members'),
                                     related_name="group_members")

    class Meta:
        verbose_name = gettext('group')
        verbose_name_plural = gettext('groups')

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=gettext('text'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=gettext('created'))

    class Meta:
        verbose_name = gettext('message')
        verbose_name_plural = gettext('messages')
        ordering = ['-created_date']

    def __str__(self):
        return str(self.created_date)+": "+self.text


class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    messages = models.ManyToManyField(UserMessage)

    class Meta:
        verbose_name = gettext('group message')
        verbose_name_plural = gettext('group messages')

    def __str__(self):
        return 'Group message'+str(self.group)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(verbose_name=gettext('biography'),
                                 null=True,
                                 blank=True)
    avatar = models.ImageField(null=True,
                               upload_to='uploads/avatars',
                               blank=True)

    class Meta:
        verbose_name = gettext('user profile')
        verbose_name_plural = gettext('user profiles')

    def __str__(self):
        return str(self.user)


class PrivateMessage(models.Model):
    participants = models.ManyToManyField(User,
                                          verbose_name=gettext('participants'),
                                          related_name="participants")
    messages = models.ManyToManyField(UserMessage)

    class Meta:
        verbose_name = gettext("private message")
        verbose_name_plural = gettext("private messages")

    def __str__(self):
        return str(self.participants)


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
