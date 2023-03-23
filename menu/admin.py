from django.contrib import admin
from django.http import HttpRequest
from .models import Menu, MenuItem
from django.db.models import QuerySet, Q

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'submenus',]
    list_display_links = ['title',]
    search_fields = ['title',]
    fields = ['title', 'slug',]
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).filter(parent=None)
    
    @admin.display(description='Подменю',)
    def submenus(self, obj):
        submenus = ''
        for submenu in obj.menu_set.all():
            submenus += f'/{submenu}/'
        return submenus
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'submenus',]
    list_display_links = ['title',]
    search_fields = ['title',]
    list_filter = ['parent',]
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).filter(~Q(parent=None))
    
    @admin.display(description='Подменю',)
    def submenus(self, obj):
        submenus = ''
        for submenu in obj.menu_set.all():
            submenus += f'/{submenu}/'
        return submenus