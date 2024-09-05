from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class recipe(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    recipe_image = models.ImageField(upload_to="recipe_img")
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField()
    recipe_direction = models.TextField()
    recipe_time = models.CharField(max_length=20)
    recipe_variety = models.CharField(max_length=10, default="veg")
    date = models.DateTimeField(_("Date"), auto_now_add=True, null=True)

class Ingredient(models.Model):
    recipe = models.ForeignKey(recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

# class Review(models.Model):
#     recipe = models.ForeignKey(recipe, related_name='review', on_delete=models.CASCADE)
#     User =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
#     text = models.TextField()
#     date = models.DateTimeField(_("Date"), auto_now_add=True, null=True)

# class Rating(models.Model):
#     recipe = models.ForeignKey(recipe, related_name='ratings', on_delete=models.CASCADE)
#     User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     rating = models.FloatField()

class Review(models.Model):
    recipe = models.ForeignKey(recipe, related_name='review', on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    date = models.DateTimeField(_("Date"), auto_now_add=True, null=True)