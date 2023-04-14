from django.urls import reverse_lazy

from .models import *


class DataMixin:
    paginate_by = 3

    def get_user_context(self ,**kwargs):
        context = kwargs
        context['genres'] = Categories.objects.all()
        return context
