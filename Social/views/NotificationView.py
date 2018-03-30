from django.shortcuts import render
from Social.models import Notification
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View
from django.db.models import Q


class NotificationView(View):

    def get(self, request):
        user = request.user
        user_notifications = Notification.objects.all().filter(receiver=user)
        unread = user_notifications.filter(status="UR")
        read = user_notifications.filter(status="RE")
        # TODO find group, event or message that created the notification
        events = []
        user_messages = []
        groups = []
        for notification in user_notifications:
            event = notification.event.all()
            print(event)
            if len(event) > 0:
                events.append(event[0])
            user_message = notification.message.all()
            if len(user_message) > 0:
                user_messages.append(user_message[0])
        print(events)
        return render(request,
                      'Social/view_notification.html',
                      {'unread': unread,
                       'read': read,
                       'events': events,
                       'user_messages': user_messages})
