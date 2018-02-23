from django.http import HttpResponse
from django.shortcuts import render
from .models import model_rating
def index(request):
    return render(request, 'SelectGame/index.html')

def all_game_rating(request):
    ratings=model_rating.objects.all()
    return render(request, 'SelectGame/all_game_rating.html',{'ratings':ratings,})
