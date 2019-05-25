from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('syn_sound', views.predict, name='predict'),
]