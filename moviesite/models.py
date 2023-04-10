from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from .aux_def import *


class Countries(models.Model):
    name = models.CharField(max_length=100 ,unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100 ,unique=True)
    slug = models.SlugField(max_length=100 ,unique=True ,db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories' ,kwargs={'slug_cat': self.slug})


class Years(models.Model):
    name = models.IntegerField(default=2000 ,unique=True)

    def __str__(self):
        return str(self.name)


class FilmDirectors(models.Model):
    name = models.CharField(max_length=100 ,unique=True)

    def __str__(self):
        return self.name


class Actors(models.Model):
    name = models.CharField(max_length=100 ,unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100 ,unique=True ,db_index=True)
    cover = models.ImageField(upload_to="cover/%Y/%m/%d")
    movie = models.FileField(upload_to="Movies/%Y/%m/%d")
    art = models.ImageField(upload_to="art/%Y/%m/%d")
    year = models.ForeignKey(Years ,on_delete=models.PROTECT)
    country = models.ForeignKey(Countries ,on_delete=models.PROTECT)
    category = models.ManyToManyField(Categories ,symmetrical=None)
    film_director = models.ManyToManyField(FilmDirectors ,symmetrical=None)
    actors = models.ManyToManyField(Actors ,symmetrical=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie' ,kwargs={'slug_movie': self.slug})


class MovieData(models.Model):
    movie = models.OneToOneField(Movie ,on_delete=models.PROTECT)
    color = models.CharField(max_length=8 ,blank=True)
    like = models.IntegerField(default=0)
    duration = models.CharField(max_length=10 ,blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.movie.slug

    def save(self ,*args ,**kwargs):
        # get dominant color with art image
        path_name = fr'moviesite\static\moviesite\buffer\{self.movie.name}.png'
        self.color = dominant_color(self.movie.art.path ,path_name)
        self.duration = time_movies(self.movie.movie.path)
        os.remove(path_name)
        ###
        super().save()


class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.PROTECT ,null=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d" ,default='placeholder.png')
    user_name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    favorite = models.ManyToManyField(Movie ,symmetrical=None)

    def __str__(self):
        return self.user_name

    def save(self ,*args ,**kwargs):
            super().save()
            img = Image.open(self.avatar.path)
            img_new = crop_center(img ,min(img.size))
            img_new.save(self.avatar.path)

    def get_absolute_url_profile(self):
        return reverse('user_profile' ,kwargs={'pk': self.pk})

    def get_absolute_url_profile_edit(self):
        return reverse('edit_profile' ,kwargs={'pk': self.pk})

    def get_absolute_url_favorite(self):
        return reverse('favorite' ,kwargs={'pk': self.pk})


@receiver(post_save ,sender=User)
def create_user_profile(sender ,instance ,created ,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save ,sender=User)
def save_user_profile(sender ,instance ,**kwargs):
    instance.userprofile.email = instance.email
    instance.userprofile.user_name = "User" + str(instance.userprofile.pk)
    instance.userprofile.save()


@receiver(post_save ,sender=Movie)
def create_movie_data(sender ,instance ,created ,**kwargs):
    if created:
        MovieData.objects.create(movie=instance)


@receiver(post_save ,sender=Movie)
def save_movie_data(sender ,instance ,**kwargs):
    instance.moviedata.save()
