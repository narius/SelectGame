from django.shortcuts import render
from SelectGame.models import Game
from SelectGame.models import Category


def add_game(request):
    if request.method == 'POST':
        print(request.FILES['image'])
        data = {'name': request.POST.get('name'),
                'category': request.POST.get('category'),
                'comment': request.POST.get('comment'),
                'image': request.FILES['image'],
                'minimum_number_of_players':
                request.POST.get('minimum_number_of_players'),
                'maximum_number_of_players':
                request.POST.get('maximum_number_of_players')
                }
        new_game = Game(name=data['name'],
                        comment=data['comment'],
                        image=data['image'],
                        minimum_number_of_players=data[
                        'minimum_number_of_players'],
                        maximum_number_of_players=data[
                        'maximum_number_of_players'])
        new_game.save()
        for pk in request.POST.getlist('category'):
            category = Category.objects.get(pk=pk)
            new_game.category.add(category)
        new_game.save()
    categories = Category.objects.all()
    return render(request,
                  'SelectGame/add_game.html',
                  {'categories': categories})
