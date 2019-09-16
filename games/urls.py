#URLs for games app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]
