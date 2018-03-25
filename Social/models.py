from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User

# Create your models here.


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


class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    messages = models.ManyToManyField(UserMessage)

    class Meta:
        verbose_name = gettext('group message')
        verbose_name_plural = gettext('group messages')

    def __str__(self):
        return 'Group message'+str(self.group)


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="user")
    friend_list = models.ManyToManyField(User,
                                         verbose_name=gettext("Friend list"),
                                         related_name="friend_list")
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


class FriendRequest(models.Model):
    STATUS = (
        ('AC', gettext("Accepted")),
        ('PE', gettext("Pending approval")),
        ('RE', gettext("Rejected")),
    )
    sender = models.ForeignKey(User,
                               related_name="sender",
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,
                                 related_name="receiver",
                                 on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS, default="AC")

    class Meta:
        verbose_name = gettext("Friend request")
        verbose_name_plural = gettext("Friend requests")
        unique_together = (("sender", "receiver"),)

    def __str__(self):
        return str(self.sender)+" - "+str(self.receiver)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_profile = 0
        rec_profile = 0
        if self.status == "AC":
            send_profile = UserProfile.objects.get_or_create(user=self.sender)[0]
            send_profile.friend_list.add(self.receiver)
            rec_profile = UserProfile.objects.get_or_create(user=self.receiver)[0]
            rec_profile.friend_list.add(self.sender)
