from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class model_group(models.Model):
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


class model_message(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(verbose_name=gettext('text'))
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=gettext('created'))
    class Meta:
        verbose_name=gettext('message')
        verbose_name_plural=gettext('messages')
        ordering = ['-created_date']
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


# Status for friends
friends_pending = 'pe'
friends_accepted = 'ac'
friends_rejected = 're'
friends_removed = 'rm'
FRIENDS_STATUS = (
    (friends_pending, gettext('pending approval')),
    (friends_accepted, gettext('accepted')),
    (friends_rejected, gettext('rejected')),
    (friends_removed, gettext('removed')),
)


class model_relationsship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=FRIENDS_STATUS,
                                            default=friends_pending)


    class Meta:
        verbose_name = gettext("Relationship status")
        verbose_name_plural = gettext("Relationship status")

    def __str__(self):
        return str(self.user)+" "+str(self.status)

class model_friend_list(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(model_relationsship)

    class Meta:
        verbose_name = gettext("Friend list")
        verbose_name_plural = gettext("Friend list")

    def __str__(self):
        return str(self.user)


class model_private_message(models.Model):
    participants=models.ManyToManyField(User, verbose_name=gettext('participants'), related_name="participants")
    messages=models.ManyToManyField(model_message)
    class Meta:
        verbose_name=gettext("private message")
        verbose_name_plural=gettext("private messages")
    def __str__(self):
        return str(self.participants)
