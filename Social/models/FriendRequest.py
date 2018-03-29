from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import User
from Social.models import UserProfile
# Create your models here.


class FriendRequest(models.Model):
    STATUS = (
        ('AC', gettext("Accepted")),
        ('PE', gettext("Pending approval")),
        ('RE', gettext("Rejected")),
    )
    sender = models.ForeignKey(User,
                               related_name="fr_sender",
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,
                                 related_name="fr_receiver",
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
