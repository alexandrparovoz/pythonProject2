from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    form = ArticleForm()
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)

