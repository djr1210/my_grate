from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Post
from math import ceil
from django.shortcuts import redirect
# Create your views here.

def index(request):
    post = Post()
    show = Post.objects.all()
    show_num = Post.objects.count()
    page = int(request.GET.get('page',1))
    per_page = 4
    pages = ceil(show_num / per_page )
    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.all().order_by('-id')[start:end]
    return render(request,'show.html',{'show':show,'posts':posts,'pages':range(pages)})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        created = request.POST.get('created')
        Post.objects.create(title=title,content=content,created=created)
        return redirect('/index')
    else:
        return render(request,'show.html')


def search(request):
    keyword = request.POST.get('search')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})

