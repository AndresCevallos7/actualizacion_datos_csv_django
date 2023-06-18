from django.urls import path
from . import views
#en esta capa se realiza el direcionamiento de las paginas.
urlpatterns = [
    path('', views.index),
    path('lista/', views.lista, name="lista"),
    path('subir/', views.subir, name="subir"),
    path('actualizar/', views.import_csv, name="actualizar"),
]