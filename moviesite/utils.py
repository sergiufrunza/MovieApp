
from.models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['genres'] = Categories.objects.all()
        return context


