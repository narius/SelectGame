from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.core.signals import request_finished
from django.contrib import messages
from django.utils.translation import gettext

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, gettext('Logged in.'), fail_silently=True,)

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, gettext('Logged out.'), fail_silently=True,)
