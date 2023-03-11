from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NewUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'

    form_class = ArticleForm

class NewDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'



def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена некорректно!'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

