from django import template
from django.template import  RequestContext
from ...models import Menu

register = template.Library()

@register.inclusion_tag(filename='templatetags/menu.html', takes_context=True)
def draw_menu(context: RequestContext, main_menu_slug: str):
    menu_and_submenu = {}

    try:
        menu_query_set = Menu.objects.select_related('parent')
        menu_and_submenu['main'] = menu_query_set.get(slug=main_menu_slug)
        menu_and_submenu['submenu'] = menu_query_set.get(slug=main_menu_slug).menu_set.all()
    except Menu.DoesNotExist:
        menu_and_submenu['error'] = f'Главноме меню с ключем "{main_menu_slug}" не найдено'
    
    return {'menu':menu_and_submenu, 'request':context['request']}

@register.inclusion_tag(filename='templatetags/submenu.html', takes_context=True)
def draw_submenu(context: RequestContext, submenu: Menu, menu_main: Menu):
    submenu_and_main = {}
    submenu_and_main['submenu'] = submenu
    submenu_and_main['main'] = menu_main
    
    return {'submenu_and_main':submenu_and_main, 'request':context['request']}