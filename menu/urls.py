from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:slug>/', views.submenu, name='submenu'),
    path('<str:slug>/<str:submenu_slug>/', views.submenu_do_something, name='submenu_do_something'),
]