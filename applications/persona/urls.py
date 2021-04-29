from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('empleados/', views.EmpleadoListView.as_view()),
    path('hojasvida/', views.ListarHojasVida.as_view()),
    path('empleados-por-depto/<short_name>/', views.EmpleadoByDeptoListView.as_view()),
    path('empleados-por-nombre/', views.EmpleadoByKwordListView.as_view()),
    path('habilidades-por-empleado/', views.HabilidadesByEmpleadoListView.as_view()),
    path('detalle-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('agregar-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='exito'),
    path('modificar-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'),
    path('eliminar-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'),


]