from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
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
