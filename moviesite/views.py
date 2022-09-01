from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.views import generic
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import *
from django.http import JsonResponse
from django.template import RequestContext
from pyexpat.errors import messages

from .models import *
from .forms import *
from .utils import *


class MainViewHome(TemplateView):
    template_name = 'moviesite/moviesite.html'
    model = MovieData

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = MovieData.objects.filter(pk__lte=4)
        context['top'] = MovieData.objects.filter(pk__gte=5)
        context['title'] = 'MovieHD'
        context['genres'] = Categories.objects.all()
        return context


class MovieView(TemplateView):
    template_name = 'moviesite/movietemplate.html'
    model = Movie
    slug_url_kwarg = 'slug_movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = get_object_or_404(Movie, slug=kwargs['slug_movie'])
        context['movie'] = movie
        context['title'] = movie.name
        context['genres'] = Categories.objects.all()

        return context


class CategoriesView(TemplateView):
    template_name = 'moviesite/categoriestemplate.html'
    model = Categories
    slug_url_kwarg = 'slug_cat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Categories, slug=kwargs['slug_cat'])
        movie_list = category.movie_set.all()
        context['movies'] = movie_list
        context['title'] = category.name
        context['genres'] = Categories.objects.all()

        return context