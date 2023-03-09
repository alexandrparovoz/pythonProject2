from django.shortcuts import render

def index(request):
    data = {
        'value': ['one', 'two', 'three'],
        'obj': {
            'car': 'audi',
            'color': 'yellow',
            'power': 190
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')


