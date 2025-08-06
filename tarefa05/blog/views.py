from django.shortcuts import render
from .models import Postagem

# Create your views here.

#def index(request):
#    posts = {Postagem.objects.all(),}
#    return render(request, "index.html", posts)

def index(request):
    context = {
        'posts': Postagem.objects.all(),
    }
    return render(request, "index.html", context)

def post(request):
    context = {
#        'post': Post.objects.all(),
    }
    return render(request, "post.html", context)