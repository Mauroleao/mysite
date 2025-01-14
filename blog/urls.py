from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
]