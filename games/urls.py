#URLs for games app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('favorites', views.favorites, name="favorites"),
    path('search', views.search, name="search"),
    path('delete/<game_id>', views.delete, name="delete"),
    path('update/<game_id>', views.update, name="update"),
]
