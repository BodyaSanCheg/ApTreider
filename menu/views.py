from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q


# Create your views here.
def main(request):
    menus = Menu.objects.filter(parent=None)

    context = {
        'menus':menus
    }
    return render(request, 'menu/main.html', context)

def submenu(request, slug):
    context = {
        'main_slug':slug,
    }
    return render(request, 'menu/submenus.html', context)

def submenu_do_something(request, slug, submenu_slug):
    context = {
        'main_slug':slug,
    }
    return render(request, 'menu/submenus.html', context)