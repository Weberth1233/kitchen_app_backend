from django.urls import path
from . import views

urlpatterns = [
    #Food urls
    path("foods/", views.fetch_foods, name="foods"),
    #------------------------------------------------
    #Category urls
    path("categorys/", views.fetch_categorys, name="categorys"),
    #------------------------------------------------
    #Recipe urls
    path("recipes/", views.fetch_recipes, name="recipes"),
    path("recipe/steps/<int:pk>", views.get_recipe_by_steps, name="get_recipe_by_steps"),
    path("recipes/category/<int:pk>", views.get_recipe_by_category, name="get_recipe_by_category"),
    path("recipes/category_filter", views.get_recipes_by_filter_categorys, name="get_recipes_by_filter_categorys"),
    #-------------------------------------------------
    #Step urls
    path("steps/", views.fetch_steps, name="steps"),
    #-------------------------------------------------
]