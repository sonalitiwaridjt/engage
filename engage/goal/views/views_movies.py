from django.shortcuts import get_object_or_404, render

from ..models import Movie, Users, Rating

import goal.utils.helper as helper
import goal.utils.recommender as recommender


def index(request):
    if 'mood' in request.GET:
        mood = request.GET.get('mood')
        genres = helper.getGenres(mood)
        user_age = Users.objects.get(username=request.user.username).age()
        allowed_ratings = helper.get_allowed_ratings(user_age)
        movies = Movie.objects.filter(
            genres__name__in=genres, content_rating__in=allowed_ratings).distinct()
        rec = movies.order_by('-popularity', '-imdb_score')[:300]
        # query = reduce(operator.and_, [Q(**{'genres__name__in': genres})])
        # movies = Movie.objects.filter(query)
        # print(movies.distinct().count())
        # return render(request, 'goal/index.html', {'movies': movies})
        context = {
            'movies': rec,
            'parameter': 'Mood'
        }
        return render(request, 'goal/recommend.html', context)
    else:
        print('no mood')
    return render(request, 'goal/index.html')


def search(request):
    if request.method == 'POST' and 'searchString' in request.POST:
        search = request.POST.get('searchString')

        user_age = Users.objects.get(username=request.user.username).age()
        allowed_ratings = helper.get_allowed_ratings(user_age)

        movies = recommender.search(search, allowed_ratings)
        context = {
            'movies': movies,
            'parameter': 'Search Query'
        }
        return render(request, 'goal/recommend.html', context)
    else:
        return render(request, 'goal/index.html')


def recommend(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movies = recommender.movie(movie_id)
        context = {
            'movies': movies,
            'parameter': 'Recommendation'
        }
        return render(request, 'goal/recommend.html', context)

    else:
        return render(request, 'goal/index.html')


def location(request):
    country = helper.get_country(request)
    print(country)
    movies = Movie.objects.filter(country=country).order_by(
        '-popularity', '-imdb_score')[:300]
    context = {
        'movies': movies,
        'parameter': 'Location'
    }
    return render(request, 'goal/recommend.html', context)


def detail(request, movie_id):
    rating = 0
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
    movie = get_object_or_404(Movie, id=movie_id)
    user = get_object_or_404(Users, username=request.user.username)
    allowed_ratings = helper.get_allowed_ratings(user.age())
    if not movie.content_rating in (allowed_ratings):
        return render(request, 'goal/index.html')
    print(movie)
    print(user)
    q = movie.rating_set.filter(user=user)
    print(q)
    ratingM = None
    if rating >= 1 and rating <= 5:
        if q.count() > 0:
            ratingM = q.first()
            ratingM.rating = rating
            print(rating)
            ratingM.save()
            movie.rating_set.add(ratingM)
            print('saved')
        else:
            ratingM = Rating(user=user, movie=movie, rating=rating)
            ratingM.save()
            movie.rating_set.add(ratingM)
            print('created')
    print(Rating.objects.all())
    context = {
        'movie': movie,
        'rating': ratingM
    }
    return render(request, 'goal/details.html', context)
