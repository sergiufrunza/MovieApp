import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from .utils import *


class Countries(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100,  unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug_cat': self.slug})


class Years(models.Model):
    name = models.IntegerField(default=2000,  unique=True)

    def __str__(self):
        return str(self.name)


class FilmDirectors(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Actors(models.Model):
    name = models.CharField(max_length=100,  unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    cover = models.ImageField(upload_to="cover/%Y/%m/%d")
    movie = models.FileField(upload_to="Movies/%Y/%m/%d")
    art = models.ImageField(upload_to="art/%Y/%m/%d")
    year = models.ForeignKey(Years, on_delete=models.PROTECT)
    country = models.ForeignKey(Countries, on_delete=models.PROTECT)
    category = models.ManyToManyField(Categories, symmetrical=None)
    film_director = models.ManyToManyField(FilmDirectors, symmetrical=None)
    actors = models.ManyToManyField(Actors, symmetrical=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug_movie': self.slug})


# class ActorsMovie(models.Model):
#     actor_id = models.ForeignKey(Actors, on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.id
#
#
# class GenreMovie(models.Model):
#     genre_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.id


class MovieData(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.PROTECT)
    color = models.CharField(max_length=8, blank=True)
    like = models.IntegerField(default=0)
    duration = models.CharField(max_length=10, blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.movie.slug

    def save(self, *args, **kwargs):
        #### get dominant color with art image ###
        path_name = fr'moviesite\static\moviesite\buffer\{self.movie.name}.png'
        self.color = dominant_color(self.movie.art.path, path_name)
        self.duration = time_movies(self.movie.movie.path)
        os.remove(path_name)
        ###
        super().save()


@receiver(post_save, sender=Movie)
def create_movie_data(sender, instance, created, **kwargs):
    if created:
        MovieData.objects.create(movie=instance)


@receiver(post_save, sender=Movie)
def save_movie_data(sender, instance, **kwargs):
    instance.moviedata.save()