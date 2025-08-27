from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list, name='libro-list'),
    path('nuevo/', views.libro_create, name='libro-create'),
    path('<int:pk>/', views.libro_detail, name='libro-detail'),
    path('<int:pk>/editar/', views.libro_update, name='libro-update'),
    path('<int:pk>/eliminar/', views.libro_delete, name='libro-delete'),
]
