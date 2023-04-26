from django import template
from django.template import  RequestContext
from ...models import Menu

register = template.Library()

@register.inclusion_tag(filename='templatetags/menu.html', takes_context=True)
def draw_menu(context: RequestContext, main_menu_slug: str, acitve_link:str):
    menu_and_submenu = {}
    parents_active_link = [acitve_link,]


    try:
        menu_query_set = Menu.objects.select_related('parent')
        menu_and_submenu['main'] = menu_query_set.get(slug=main_menu_slug)
        menu_and_submenu['submenu'] = menu_query_set.get(slug=main_menu_slug).menu_set.all()

        while acitve_link:

            try:
                acitve_link = menu_query_set.get(slug=acitve_link).parent
                if acitve_link:
                    acitve_link = acitve_link.slug
                    parents_active_link.append(acitve_link)
            except:
                acitve_link = None
        
        if not acitve_link:
            parents_active_link.append(main_menu_slug)
            
        menu_and_submenu['parents_active_link'] = parents_active_link

    except Menu.DoesNotExist:
        menu_and_submenu['error'] = f'Главноме меню с ключем "{main_menu_slug}" не найдено'
    
    return {'menu':menu_and_submenu, 'request':context['request']}

@register.inclusion_tag(filename='templatetags/submenu.html', takes_context=True)
def draw_submenu(context: RequestContext, submenu: Menu, parents_active_link: list):
    submenu_and_parents = {}
    submenu_and_parents['submenu'] = submenu
    submenu_and_parents['parents_active_link'] = parents_active_link
    submenu_and_parents['main'] = parents_active_link[-1]
    
    return {'submenu_and_parents':submenu_and_parents, 'request':context['request']}