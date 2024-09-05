from django.contrib import admin
from .models import recipe, Ingredient, Review
# Register your models here.

admin.site.register(recipe)
admin.site.register(Ingredient)
admin.site.register(Review)