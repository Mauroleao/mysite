from django.http import HttpResponse
from django.views import generic

class ExercicioView(generic.View):
    def get(self, request):
        return HttpResponse("Bem Vindo a Pagina exercicio")