from django.http import Http404
from django.shortcuts import render

from .forms import RegisterForm


def register_view(request):
    form = RegisterForm()
        
    return render(request, 'authors/pages/register_view.html', {
        'form': form
    })

def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm(request.POST)
    
    return render(request, 'authors/pages/register_view.html', {
        'form': form
    })