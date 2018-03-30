from django.shortcuts import render
from Social.models import Notification
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View
from django.db.models import Q


class NotificationView(View):

    def get_notifications(self):
        user_notifications = Notification.objects.all().filter(receiver=self.user)
        unread = user_notifications.filter(status="UR")
        read = user_notifications.filter(status="RE")
        events = []
        user_messages = []
        groups = []
        for notification in unread:
            event = notification.event.all()
            print(event)
            if len(event) > 0:
                events.append([event[0], notification])
            user_message = notification.message.all()
            if len(user_message) > 0:
                user_messages.append([user_message[0], notification])
            group = notification.group.all()
            if len(user_message) > 0:
                groups.append([group, notification])
        print(events)
        self.notifications = {'unread': unread,
                              'read': read,
                              'events': events,
                              'user_messages': user_messages,
                              'groups': groups}

    def get(self, request):
        self.user = request.user
        self.get_notifications()
        return render(request,
                      'Social/view_notification.html',
                      self.notifications)

    def post(self, request):
        self.user = request.user
        user_notifications = Notification.objects.all().\
                             filter(receiver=self.user)
        for notification in user_notifications:
            if request.POST.get("read_"+str(notification.id)):
                notification.status = "RE"
                notification.save()
        self.get_notifications()
        return render(request,
                      'Social/view_notification.html',
                      self.notifications)
