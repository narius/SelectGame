##a file for function around ratings
import numpy
from .models import model_rating
from .models import model_game
class rating_functions():
    def mean_rating_per_game(games):
        mean_rating_per_game=[]
        for game in games:
            ratings=model_rating.objects.filter(game=game).values('rating')
            total=len(ratings)
            if (total!=0):
                mean_rating=sum(rating['rating'] for rating in ratings) /total
            else:
                mean_rating=0
            mean_rating_per_game.append([game,mean_rating, total])
        return mean_rating_per_game
