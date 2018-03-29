from django.shortcuts import render
from Social.models import Notification


def index(request):
    user = request.user
    notifications = Notification.objects.all().\
        filter(receiver=user).\
        filter(status="UR")
    return render(request,
                  'SelectGame/index.html',
                  {'number_of_notification': len(notifications)})
