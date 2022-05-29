from django.db.models import Q
from ..models import Movie
from ..utils import helper
from django.db.models import Case, When


def movie(movie_id):
    movies = Movie.objects.all()
    curr = movies.count()
    if curr > helper.get_last_count():
        helper.set_last_count(curr)
        print('New movie added')
        # TODO: Add new movie to recommender
        helper.add_new_movie(movies)
    else:
        print('No new movie added')

    data = helper.get_transformed_data()
    data = data.transpose()
    movie = Movie.objects.get(id=movie_id)

    def recommendation_movie(movie):
        movie = data[movie]
        similar_movies = data.corrwith(movie)
        similar_movies = similar_movies.sort_values(ascending=False)
        similar_movies = similar_movies.iloc[1:]
        return list(similar_movies.index[:300])

    data = recommendation_movie(movie.movie_title)

    order = Case(*[When(movie_title=movie_title, then=pos)
                 for pos, movie_title in enumerate(data)])
    movies = Movie.objects.filter(movie_title__in=data).order_by(order)

    return movies


def search(search, allowed_ratings):
    return Movie.objects.filter(Q(color__icontains=search) | Q(director_name__icontains=search) | Q(actor_2_name__icontains=search) | Q(genres__name__icontains=search) | Q(actor_1_name__icontains=search) | Q(movie_title__icontains=search) | Q(actor_3_name__icontains=search) | Q(plot_keywords__name__icontains=search) | Q(language__icontains=search) | Q(country__icontains=search) | Q(content_rating__icontains=search)).filter(content_rating__in=allowed_ratings).distinct().order_by(
        '-popularity', '-imdb_score')[:300]
