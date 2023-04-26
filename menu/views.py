from django.shortcuts import render
from .models import *


def main(request):
    # Главная функция вывода основного дерева
    menus = Menu.objects.filter(parent=None)

    context = {
        'menus':menus
    }
    return render(request, 'menu/main.html', context)

def submenu(request, slug):
    # Функция вывода подменю
    context = {
        'main_slug':slug,
    }
    return render(request, 'menu/submenus.html', context)

def submenu_do_something(request, slug, submenu_slug):
    # Переход на ветку дерева подменю
    context = {
        'main_slug':slug,
        'active_link':submenu_slug,
    }
    return render(request, 'menu/submenus.html', context)