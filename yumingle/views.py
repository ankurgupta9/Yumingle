from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
import os

# Create your views here.

# def home(request):
#     recipes = recipe.objects.all()
#     if request.GET.get('search'):
#         recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
#         return render(request,"search_res.html",{'recipes': recipes})

#     return render(request, "index.html", {'recipes': recipes})

def home(request):
    recipes = recipe.objects.all()

    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains=request.GET.get('search'))
        return render(request, "search_res.html", {'recipes': recipes})

    # Calculate average ratings for recipes
    average_ratings = recipe.objects.annotate(avg_rating=Avg('review__rating')).values_list('id', 'avg_rating')

    context = {
        'recipes': recipes,
        'average_ratings': average_ratings
    }

    return render(request, "index.html", context)

@login_required(login_url="/login")
def add_recipe(request):

    if request.method == 'POST':
         data = request.POST
         recipe_image = request.FILES.get('recipe_image')
         recipe_name = data.get('recipe_name')
         recipe_description = data.get('recipe_description')
         recipe_direction = data.get('recipe_direction')
         recipe_time = data.get('recipe_time')
         recipe_variety = data.get('variety')

         new_recipe=recipe.objects.create(
            User=request.user,
            recipe_image =recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_direction = recipe_direction,
            recipe_time = recipe_time,
            recipe_variety = recipe_variety,
         )

         ingredients = request.POST.getlist('ingredients[]')
         
         for ingredient in ingredients:
            Ingredient.objects.create(recipe=new_recipe, name=ingredient)

         return redirect('/add')
    
    queryset = recipe.objects.all()
    context = {'add_recipe':queryset}
         
    return render(request,"Add_recipe.html")

def my_search(request):
    recipes = recipe.objects.all()
    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
    return render("search_res.html",{'recipes': recipes})

@login_required(login_url="/login")
def my_recipe(request):
    current_user = request.user
    user_recipes = recipe.objects.filter(User=current_user)
    return render(request, "my_recipe.html", {'recipes': user_recipes})

# def recipe_detail(request, id):
#     recipe_obj = recipe.objects.get(id=id)
#     ingredients = recipe_obj.ingredients.all() 
#     reviews = Review.objects.filter(recipe=recipe_obj) 

#     context = {'recipe': recipe_obj, 'ingredients': ingredients, 'reviews': reviews}
#     return render(request, "detail_page.html", context)

# def recipe_detail(request, id):
#     recipe_obj = recipe.objects.get(id=id)
#     ingredients = recipe_obj.ingredients.all()
#     reviews = Review.objects.filter(recipe=recipe_obj)
#     ratings = Rating.objects.filter(recipe=recipe_obj)

#     user_rating = None
#     if request.user.is_authenticated:
#         user_rating = Rating.objects.filter(recipe=recipe_obj, User=request.user).first()

#     context = {
#         'recipe': recipe_obj,
#         'ingredients': ingredients,
#         'reviews': reviews,
#         'ratings': ratings,
#         'user_rating': user_rating
#     }
#     return render(request, "detail_page.html", context)

def recipe_detail(request, id):
    recipe_obj = recipe.objects.get(id=id)
    ingredients = recipe_obj.ingredients.all()
    reviews = Review.objects.filter(recipe=recipe_obj)

    average_ratings = recipe.objects.annotate(avg_rating=Avg('review__rating')).values_list('id', 'avg_rating')
    
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(recipe=recipe_obj, User=request.user).first()

    context = {
        'recipe': recipe_obj,
        'ingredients': ingredients,
        'reviews': reviews,
        'user_review': user_review,
        'average_ratings': average_ratings
    }
    return render(request, "detail_page.html", context)

@login_required(login_url="/login")
def delete_recipe(request, id):
    queryset = recipe.objects.get(id = id)
    if queryset.recipe_image:
        image_path = queryset.recipe_image.path
        if os.path.exists(image_path):
            os.remove(image_path)

    queryset.delete()
    return redirect('/view')

@login_required(login_url="/login")
def update_recipe(request, id):
    queryset = recipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_direction = data.get('recipe_direction')
        recipe_time = data.get('recipe_time')
        recipe_variety = data.get('variety')
        
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        queryset.recipe_direction = recipe_direction
        queryset.recipe_time = recipe_time
        queryset.recipe_variety = recipe_variety

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        
        return redirect('/view')

    context = {'recipe':queryset}
    return render(request, "update_recipe.html", context)

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid username")
            return redirect('/login')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid password")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')

    return render(request, "login.html")

def Register_page(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register')

        user = User.objects.create(
            first_name = fullname,
            username = username, 
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")
        return redirect('/register')

    return render(request, "registration.html")

def Logout_page(request):
    logout(request)
    return redirect('/')

# @login_required(login_url="/login")
# def add_review(request, id):
#     if request.method == 'POST':
#         text = request.POST.get('review_text')
#         user = request.user
#         recipe_obj = recipe.objects.get(id=id)
#         # Create a new review
#         Review.objects.create(recipe=recipe_obj, User=user, text=text)
        
#         # messages.success(request, 'Review added successfully.')        
#         return redirect('recipe_detail', id=id)

# @login_required(login_url="/login")
# def rate_recipe(request, id):
#     if request.method == 'POST':
#         recipe_obj = recipe.objects.get(id=id)
#         rating_value = float(request.POST.get('rating'))

#         # Check if the rating is valid (e.g., between 1 and 5)
#         if 1 <= rating_value <= 5:
#             # Check if the user already rated this recipe
#             existing_rating = Rating.objects.filter(recipe=recipe_obj, User=request.user).first()

#             if existing_rating:
#                 # Update existing rating
#                 existing_rating.rating = rating_value
#                 existing_rating.save()
#             else:
#                 # Create new rating
#                 Rating.objects.create(recipe=recipe_obj, User=request.user, rating=rating_value)

#     return redirect('recipe_detail', id=id)

@login_required(login_url="/login")
def add_review(request, id):
    if request.method == 'POST':
        text = request.POST.get('review_text')
        rating_value = float(request.POST.get('rating',0.0))
        user = request.user
        recipe_obj = recipe.objects.get(id=id)
        
        # Ensure the rating is within valid range
        if 0 <= rating_value <= 5:
            # Create a new review
            existing_review = Review.objects.filter(recipe=recipe_obj, User=request.user).first()

            if existing_review:
                # Update existing rating
                existing_review.rating = rating_value
                existing_review.text = text
                existing_review.save()
            else:
                # Create new rating
                Review.objects.create(recipe=recipe_obj, User=user, text=text, rating=rating_value)


        
        # messages.success(request, 'Review added successfully.')        
        return redirect('recipe_detail', id=id)
