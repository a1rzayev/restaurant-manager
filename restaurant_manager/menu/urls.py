from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('categories/', views.category_list, name='category_list'),
    path('dishes/', views.dish_list, name='dish_list'),
    
    
    # Admin paths
    path('admin/register/', views.admin_register, name='admin_register'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('admin/add_category/', views.add_category, name='add_category'),
    path('admin/add_dish/', views.add_dish, name='add_dish'),
    path('admin/delete_restaurant/<int:id>/', views.delete_restaurant, name='delete_restaurant'),
    path('admin/delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('admin/delete_dish/<int:id>/', views.delete_dish, name='delete_dish'),
]
