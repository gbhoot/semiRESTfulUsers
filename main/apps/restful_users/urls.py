from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('users/', views.index),
    path('users/new/', views.new),
    path('users/new/create/', views.add),
    path('users/<int:id>/', views.show),
    path('users/<int:id>/edit/', views.edit),
    path('users/<int:id>/edit/update/', views.update),
    path('users/<int:id>/delete/', views.delete),
]