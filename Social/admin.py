from django.contrib import admin
from Social.models import UserProfile
from Social.models import Group
from Social.models import UserMessage
from Social.models import GroupMessage
from Social.models import PrivateMessage
from Social.models import FriendRequest
from Social.models import Notification
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(UserMessage)
admin.site.register(GroupMessage)
admin.site.register(PrivateMessage)
admin.site.register(FriendRequest)
admin.site.register(Notification)
