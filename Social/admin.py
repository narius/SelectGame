from django.contrib import admin
from Social.models import UserProfile
from Social.models import Group
from Social.models import UserMessage
from Social.models import GroupMessage
from Social.models import PrivateMessage
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(UserMessage)
admin.site.register(GroupMessage)
admin.site.register(PrivateMessage)
