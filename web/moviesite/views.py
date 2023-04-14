from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView ,ListView ,CreateView ,TemplateView, UpdateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import *
from django.http import JsonResponse
from django.template import RequestContext
from pyexpat.errors import messages
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.response import *
from .forms import *
from .utils import *
from .models import *


class MainViewHome(DataMixin ,TemplateView):
    template_name = 'moviesite/moviesite.html'
    model = MovieData

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['top'] = MovieData.objects.filter(pk__gte=5)
        context['movies'] = MovieData.objects.filter(pk__lte=4)
        mix = self.get_user_context(title="MovieHD")

        return dict(list(context.items()) + list(mix.items()))

    # def get(self, request, *args, **kwargs):
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get_queryset(self):
        return MovieData.objects.filter(pk__lte=4)


class MovieView(DataMixin ,DetailView):
    template_name = 'moviesite/movie.html'
    model = Movie
    slug_url_kwarg = 'slug_movie'
    context_object_name = 'movie'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title=context['movie'])

        return dict(list(context.items()) + list(mix.items()))


class CategoriesView(DataMixin ,ListView):
    template_name = 'moviesite/category.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['slug_cat']
        mix = self.get_user_context(title=get_object_or_404(Categories ,slug=self.kwargs['slug_cat']).name)
        return dict(list(context.items()) + list(mix.items()))

    def get_queryset(self):
        return Movie.objects.filter(category__slug=self.kwargs['slug_cat'] ,pk__lte=4)


class FavoriteView(DataMixin ,ListView):
    template_name = 'moviesite/favorite.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title="favorite")
        return dict(list(context.items()) + list(mix.items()))

    def get_queryset(self):
        user = get_object_or_404(UserProfile ,pk=self.kwargs['pk'])
        print(user.favorite.all())
        return user.favorite.all()


class ProfileUser(DataMixin ,DetailView):
    template_name = 'moviesite/profile.html'
    model = UserProfile
    pk_url_kwarg = 'pk'
    context_object_name = 'user'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title=self.kwargs['pk'])
        return dict(list(context.items()) + list(mix.items()))


class LoginUser(DataMixin ,LoginView):
    form_class = AuthForm
    template_name = 'moviesite/login.html'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title="Sing In")
        return dict(list(context.items()) + list(mix.items()))

    def get_success_url(self):
        return self.request.GET["next"]


class RegisterUser(DataMixin ,CreateView):
    form_class = RegisterUserForm
    template_name = 'moviesite/registrate.html'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(mix.items()))

    def form_valid(self, form):
        valid = super(RegisterUser, self).form_valid(form)
        login(self.request, self.object)
        return valid

    def get_success_url(self):
        return self.request.GET["next"]


class EditUserProfile(DataMixin ,UpdateView):
    model = UserProfile
    form_class = EditFormProfile
    template_name = 'moviesite/editprofile.html'

    def get_context_data(self ,* ,object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context(title="EditProfile")
        return dict(list(context.items()) + list(mix.items()))

    def form_valid(self, form):
        valid = super(EditUserProfile, self).form_valid(form)
        self.object.save()
        return valid

    def get_success_url(self):
        return self.request.GET["next"]




class FavoriteAPI(APIView):
    def put(self ,request ,**kwargs):
        slug = self.kwargs["slug_favorite"]
        movie = get_object_or_404(Movie ,slug=slug)
        self.request.user.userprofile.favorite.add(movie)
        return JsonResponse({})

    def delete(self ,request ,**kwargs):
        slug = self.kwargs["slug_favorite"]
        movie = get_object_or_404(Movie ,slug=slug)
        self.request.user.userprofile.favorite.remove(movie)
        return JsonResponse({})


def log_out_user(request):
    logout(request)
    return redirect("main_page")
