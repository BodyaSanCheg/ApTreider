from django.db import models

# Create your models here.
class Menu(models.Model):
    """Описание каждого поля Меню"""
    title = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='EN. Адрес')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name_plural = 'Меню'
        verbose_name = 'Меню'

    def __str__(self):
        return self.title
    
    def get_submenu(self):
        return self.menu_set.get_queryset()

class MenuItem(Menu):
    """Модель, создает экземпляр у основного меню"""
    class Meta:
        verbose_name_plural = 'Подменю'
        verbose_name = 'Подменю'
        proxy = True