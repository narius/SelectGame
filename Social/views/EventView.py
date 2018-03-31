from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserMessage
from Social.models import UserProfile
from Social.models import Notification
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View
from django.contrib.auth.models import User
from SelectGame.models import EventParticipant
from SelectGame.models.EventParticipant import EVENT_STATUS_MAYBE
from SelectGame.models.EventParticipant import EVENT_STATUS_WILL_COME
from SelectGame.models.EventParticipant import EVENT_STATUS_NOT_COMING
from SelectGame.models.EventParticipant import EVENT_STATUS_PENDING


class EventView(View):
    '''
        Displays a specifik event.
    '''
    # TODO join button, only if there is room
    def filter_friends(self):
        profile = UserProfile.objects.get_or_create(user=self.user)[0]
        friends = profile.friend_list.all()
        participants = self.event.participants.all()
        fr = []
        for friend in friends:
            if friend not in participants:
                fr.append(friend)
        return fr

    def get(self, request, event_id):
        self.user = request.user
        self.event = Event.objects.get(pk=event_id)
        friends = self.filter_friends()
        print("innan get return")
        return render(request,
                      'Social/view_event.html',
                      {'event': self.event,
                       'friends': friends})

    def post(self, request, event_id):
        self.user = request.user
        self.event = Event.objects.get(pk=event_id)
        friends = self.filter_friends()
        if request.POST.get("cancel"):
            return render(request,
                          'Social/view_event.html',
                          {'event': self.event,
                           'friends': friends})
        if request.POST.get("new_message"):
            text = request.POST.get("message")
            new_message = UserMessage(writer=self.user, text=text)
            new_message.save()
            self.event.messages.add(new_message)
        if request.POST.get("invite_friends"):
            for pk in request.POST.getlist('friends'):
                invite = User.objects.get(pk=pk)
                notification = Notification(sender=self.user,
                                            receiver=invite)
                notification.save()
                self.event.notifications.add(notification)
                participant = EventParticipant.objects.get_or_create(
                              user=invite, event=self.event)
            self.event.save()
        if request.POST.get(EVENT_STATUS_WILL_COME):
            participant = EventParticipant.objects.get(
                          user=self.user,
                          event=self.event)
            participant.status = EVENT_STATUS_WILL_COME
            participant.save()
        if request.POST.get(EVENT_STATUS_MAYBE):
            participant = EventParticipant.objects.get(
                          user=self.user,
                          event=self.event)
            participant.status = EVENT_STATUS_MAYBE
            participant.save()
        if request.POST.get(EVENT_STATUS_NOT_COMING):
            participant = EventParticipant.objects.get(
                          user=self.user,
                          event=self.event)
            participant.status = EVENT_STATUS_NOT_COMING
            participant.save()
        participants = self.event.participants.all().filter(user=self.user)
        if len(participants) == 0:
            return HttpResponse(gettext("You are not part of this event"))

        return render(request,
                      'Social/view_event.html',
                      {'event': self.event,
                       'friends': friends})
