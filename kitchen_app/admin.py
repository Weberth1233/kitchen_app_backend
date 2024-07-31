from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Steps)
admin.site.register(RecipeIngredients)