from django.shortcuts import render
from .models import Restaurant, Category, Dish

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'menu/restaurant_list.html', {'restaurants': restaurants})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/category_list.html', {'categories': categories})

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})
