from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list, name='libro-list'),
    path('nuevo/', views.libro_create, name='libro-create'),
    path('edicionLibro/<int:libro_id>/', views.edicionLibro, name='libro-update'),
    path('editarLibro/', views.editarLibro, name='libro-save'),
    path('eliminarLibro/<int:libro_id>/', views.eliminarLibro, name='libro-delete'),
]
