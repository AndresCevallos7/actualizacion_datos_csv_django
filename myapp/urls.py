from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lista/', views.lista, name="lista"),
    path('subir/', views.subir, name="subir"),
    path('actualizar/', views.import_csv, name="actualizar"),
]