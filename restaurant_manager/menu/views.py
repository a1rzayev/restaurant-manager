from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Category, Dish
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'menu/restaurant_list.html', {'restaurants': restaurants})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/category_list.html', {'categories': categories})

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})

def admin_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_superuser(username=username, password=password)
        return redirect('admin_login')
    return render(request, 'menu/admin_register.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('restaurant_list')
    return render(request, 'menu/admin_login.html')

@login_required
def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        Restaurant.objects.create(name=name, address=address, phone=phone)
        return redirect('restaurant_list')
    return render(request, 'menu/add_restaurant.html')

@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'menu/add_category.html')

@login_required
def add_dish(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        restaurant_id = request.POST['restaurant']
        category = get_object_or_404(Category, id=category_id)
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        Dish.objects.create(name=name, description=description, price=price, category=category, restaurant=restaurant)
        return redirect('dish_list')
    return render(request, 'menu/add_dish.html', {'categories': Category.objects.all(), 'restaurants': Restaurant.objects.all()})

@login_required
def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    restaurant.delete()
    return redirect('restaurant_list')

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')

@login_required
def delete_dish(request, id):
    dish = get_object_or_404(Dish, id=id)
    dish.delete()
    return redirect('dish_list')

