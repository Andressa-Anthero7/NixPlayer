from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_audio', views.adicionar_audio, name='adicionar_audio'),

]
