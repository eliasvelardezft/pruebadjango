from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.PruebaView.as_view()),
    path('lista', views.PruebaListView.as_view()),
    path('personas', views.ListarPersonas.as_view()),
    path('agregarpersona', views.CreatePerson.as_view()),
]