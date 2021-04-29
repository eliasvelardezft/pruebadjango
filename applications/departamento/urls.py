from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('nuevo-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name="nuevo_departamento"),
]
