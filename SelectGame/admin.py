from django.contrib import admin
from  .models import Category, Event
from .models import Game, Location,Rating
from .models import  GameLibrary
# Register your models here.
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Location)
admin.site.register(Rating)
admin.site.register(Event)
admin.site.register( GameLibrary)
