from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    dob = models.DateField()

    def age(self) -> int:
        "Return the current age of this user."
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    color = models.CharField(max_length=100, null=True, blank=True)
    director_name = models.CharField(max_length=100)
    num_critic_for_reviews = models.IntegerField()
    duration = models.IntegerField()
    director_facebook_likes = models.IntegerField()
    actor_3_facebook_likes = models.IntegerField()
    actor_2_name = models.CharField(max_length=100)
    actor_1_facebook_likes = models.IntegerField()
    gross = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    actor_1_name = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=100)
    num_voted_users = models.IntegerField()
    cast_total_facebook_likes = models.IntegerField()
    actor_3_name = models.CharField(max_length=100)
    facenumber_in_poster = models.IntegerField()
    plot_keywords = models.ManyToManyField(Keyword)
    movie_imdb_link = models.CharField(max_length=100)
    num_user_for_reviews = models.IntegerField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    content_rating = models.CharField(max_length=100)
    budget = models.IntegerField()
    title_year = models.IntegerField()
    actor_2_facebook_likes = models.IntegerField()
    imdb_score = models.FloatField()
    aspect_ratio = models.FloatField()
    movie_facebook_likes = models.IntegerField()
    popularity = models.FloatField()
    rated = models.ManyToManyField(Users, through='Rating')

    def age_limit(self) -> int:
        "Returns the minimum age required for this movie."
        return {
            'Approved': 0,
            'G': 2,
            'GP': 7,
            'PG': 10,
            'PG-13': 13,
            'Unrated': 14,
            'Not Rated': 15,
            'Passed': 15,
            'R': 16,
            'X': 17,
            'NC-17': 17,
            'M': 18
        }.get(self.content_rating, 18)

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['movie_title']

    def __str__(self):
        return self.movie_title


class Rating(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return self.user.username + ' ' + self.movie.movie_title
