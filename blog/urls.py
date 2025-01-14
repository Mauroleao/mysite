from django.urls import path
from .views import PostView, ExercicioView

urlpatterns = [
    path('home/', PostView.as_view(), name='home'),
    path('exercicio/', ExercicioView.as_view(), name='exercicio'),
]