from django.shortcuts import render


def home(request):
    
    context = {
        'name': 'Lucas Santana'
    }
    
    return render(request, 'recipes/pages/home.html', context)


def recipe(request, id):
    
    context = {
        'name': 'Lucas Santana'
    }
    
    return render(request, 'recipes/pages/recipe-view.html', context)