from django.http import HttpResponse
from django.views import gereric


class PostView(gereric.View):
    def get(self, request, *args, **kwargs):
        return None