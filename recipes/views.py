from django.shortcuts import render


def home(request):
    
    context = {
        'name': 'Lucas Santana'
    }
    
    return render(request, 'recipes/home.html', context)