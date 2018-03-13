from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import model_friend_list
from .models import model_relationsship

#When a new relationsship i created we want to uppdate both friendslist
#
@receiver(post_save, sender=model_relationsship)
def sync_friends_list(sender, instance, created, **kwargs):
    '''
        user is the user that I'm adding to my list of friends
    '''
    user = instance.user
    friend_list = model_friend_list.objects.get_or_create(user=user)
    
