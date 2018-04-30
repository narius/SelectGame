from django.shortcuts import render
from Social.models import UserMessage
from Social.models import PrivateMessage
from django.views import View


class PrivateMessageView(View):
    '''
        View to display private messages
    '''
    def get(self, request):
        user = request.user
        # Get all PrivateMessages where user user is a participants
        private_messages = user.private_messages.all()
        print("private_messages")
        print(private_messages)
        return render(request, 'Social/view_privatemessages.html', {
            "private_messages": private_messages,
            })

    def post(self, request):
        user = request.user
        private_messages = user.private_messages.all()
        for private_message in private_messages:
            if request.POST.get("new_message_"+str(private_message.id)):
                text = request.POST.get("new_message_text_"
                                        + str(private_message.id))
                new_message = UserMessage(writer=user, text=text)
                new_message.save()
                private_message.messages.add(new_message)
        return render(request, 'Social/view_privatemessages.html', {
            "private_messages": private_messages,
            })
