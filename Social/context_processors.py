from Social.models import Notification


def notifications_context_processor(request):
    user = request.user
    notifications = Notification.objects.all().\
        filter(receiver=user).\
        filter(status="UR")
    return {
        'number_of_notification': len(notifications),
    }
