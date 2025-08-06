from django.shortcuts import render
from datetime import date
from .models import Tarefa

# Create your views here.
def index(request):
    context = {
        'tarefas': Tarefa.objects.all(),
    }
    context['hoje'] = date.today()
    return render(request, "index.html", context)