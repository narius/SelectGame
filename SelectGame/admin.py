from django.contrib import admin
from .models import Category
from .models import Event
from .models import EventGame
from .models import EventGameVote
from .models import EventParticipant
from .models import Game
from .models import Location
from .models import Rating
from .models import GameLibrary

# Register your models here.
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Location)
admin.site.register(Rating)
admin.site.register(Event)
admin.site.register(EventGame)
admin.site.register(EventGameVote)
admin.site.register(EventParticipant)
admin.site.register(GameLibrary)
