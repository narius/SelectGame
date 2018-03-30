from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.core.signals import request_finished
from django.contrib import messages
from django.utils.translation import gettext


# TODO create notifications for invites and messages
