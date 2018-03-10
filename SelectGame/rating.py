##a file for function around ratings
import numpy
from .models import model_rating
from .models import model_game
from .models import model_game_library
class rating_functions():
    #Function to calulate the average for games
    def mean_rating_per_game(games):
        mean_rating_per_game=[]
        for game in games:
            ratings=model_rating.objects.filter(game=game).values('rating')
            total=len(ratings)
            votes=[0,0,0,0,0]
            width=[0,0,0,0,0]
            if (total!=0):
                for rating in ratings:
                    print(rating['rating'])
                    votes[rating['rating']-1]=votes[rating['rating']-1]+1
                n=0
                while n<5:
                    width[n]=int(round((votes[n]/total)*100))
                    n=n+1
                mean_rating=sum(rating['rating'] for rating in ratings) /total
            else:
                mean_rating=0
            mean_rating_per_game.append({'game':game,
                                        'mean_rating':mean_rating,
                                        'total':total,
                                        'votes':votes,
                                        'width':width})
        return mean_rating_per_game

    def users_rating(users, lower_limit):
        """
            This function will return the average rating for all games that :model:`auth.User` have
            rated higher than lower_limit
        """
        games = []
        ratings = {}
        number_of_votes = {}
        avarage = []
        for user in users:
            #Retrieve all games that the users own.
            game_library=model_game_library.objects.get_or_create(owner=user)[0]
            for game in game_library.games.all():
                user_ratings=model_rating.objects.all().filter(user=user).filter(game=game)
                for rating in user_ratings:
                    if rating.rating > lower_limit:
                        print(rating.game.name)
                        ratings[rating.game.name] = ratings.setdefault(rating.game.name,0)+rating.rating
                        number_of_votes[rating.game.name] = number_of_votes.setdefault(rating.game.name,0)+1
                if game not in games:
                    print("rating-append: "+str(game))
                    games.append(game)
        #By now whe should have two list, one with all available game,
        #one with all ratings.
        print(ratings)
        for game in games:
            #Find all ratings for this game
            game_avarage = ratings.setdefault(game.name,0)/number_of_votes.setdefault(game.name,1)
            votes=number_of_votes[game.name]
            too_low=True if game_avarage==0 else False
            avarage.append({'game':game,
                            'number_of_votes':votes,
                            'average': game_avarage,
                            'too_low': too_low
            })
        return avarage
