from django.contrib import admin
from .models import Category
from .models import Event
from .models import Game
from .models import Location
from .models import Rating
from .models import GameLibrary
from .models import EventParticipant
# Register your models here.
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Location)
admin.site.register(Rating)
admin.site.register(Event)
admin.site.register(GameLibrary)
admin.site.register(EventParticipant)
