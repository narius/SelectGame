from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserProfile
from Social.models import FriendRequest
from Social.models import Notification
from django.utils.translation import gettext
from django.views import View
from django.db.models import Q


class NotificationView(View):

    def get(self, request):
        user = request.user
        notifications = Notification.objects.all().filter(receiver=user)
        unread = notifications.filter(status="UR")
        read = notifications.filter(status="RE")
        # TODO find group, event or message that created the notification
        return render(request,
                      'Social/view_notification.html',
                      {'unread': unread,
                      'read': read})
