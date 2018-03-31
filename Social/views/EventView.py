from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserMessage
from Social.models import UserProfile
from Social.models import Notification
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from SelectGame.models import EventParticipant
from SelectGame.models.EventParticipant import STATUS as PARTCIPANTS_STATUS
from SelectGame.models.EventParticipant import EVENT_STATUS_WILL_COME


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
        participants = self.event.participants.all()
        coming = self.event.participants.all()\
                 .filter(status=EVENT_STATUS_WILL_COME)
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
        participant = EventParticipant.objects.get(
                      user=self.user,
                      event=self.event)
        for status in PARTCIPANTS_STATUS:
            if request.POST.get(status[0]):
                participant = EventParticipant.objects.get(
                              user=self.user,
                              event=self.event)
                if (len(coming) >= self.event.maximum_number_of_players
                        and status[0] == EVENT_STATUS_WILL_COME):
                    messages.add_message(request,
                                         messages.WARNING,
                                         gettext('The event is full'))
                    break
                participant.status = status[0]
                participant.save()
        participants = self.event.participants.all().filter(user=self.user)
        if len(participants) == 0:
            return HttpResponse(gettext("You are not part of this event"))

        return render(request,
                      'Social/view_event.html',
                      {'event': self.event,
                       'friends': friends})
