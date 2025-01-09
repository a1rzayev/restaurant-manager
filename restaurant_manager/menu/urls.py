from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('categories/', views.category_list, name='category_list'),
    path('dishes/', views.dish_list, name='dish_list'),
]
