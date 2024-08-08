from django.db import models
from django.utils import timezone
import datetime
from operator import itemgetter, attrgetter
from django.core.paginator import Paginator

class Base(models.Model):
    def pagination(page_number, list):
        paginator = Paginator(list, 2)
        page_obj = paginator.get_page(page_number)
        return page_obj


class Food(models.Model):
    name = models.CharField(max_length=50)
    more_info = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'Nome da comida = {self.name} - informações adicionais = {self.more_info}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Nome da categoria = {self.name}'
    
class Step(models.Model):
    description = models.CharField(max_length=200)
    number_step = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Descrição = {self.description} - etapa = {self.number_step}'
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    ingredients = models.ManyToManyField(Food, related_name='recipe')
    steps = models.ManyToManyField(Step, related_name='steps_recipe')
    time_to_prepare = models.IntegerField()
    created_at = models.DateTimeField()

    def was_recipe_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    
    def get_image_url(self):
        return self.image.url if self.image else None

    def get_ordered_steps(self):
        return self.steps.order_by('number_step')

    def recently_recipes(**kwargs):
        recipes =Recipe.objects.get_queryset().order_by('id')
        recently_recipes = []
        for recipe in recipes:
            validate = recipe.was_recipe_recently()
            if(validate):
                recently_recipes.append(recipe)
        return sorted(recently_recipes, key = attrgetter('created_at'))
        
    def get_recipes_by_category(id_category=None):
        recipes = Recipe.objects.all()
        recipes_by_category = []
        for recipe in recipes: 
            if(recipe.category.id == id_category):    
                recipes_by_category.append(recipe)
        return recipes_by_category
    
    def get_recipes_by_filter_categorys(categorys_id = []):
        recipe_filter_category = []
        recipes = Recipe.objects.all()
        for recipe in recipes: 
            for id in categorys_id:
                if recipe.category.id == id:
                    recipe_filter_category.append(recipe)
        return recipe_filter_category

# recipes = Recipe.objects.all()
#     paginator = Paginator(recipes, 10)
#     page_number = request.data.get("page")
#     page_obj = paginator.get_page(page_number)            
    #get recipes by parameters

    def pagination(page_number, list):
        paginator = Paginator(list, 2)
        page_obj = paginator.get_page(page_number)
        return page_obj

    #Ordenar por tempo de preparo da comida

    def filter_recipes_by_name(name=None):
        try:
            if name is not None:
                recipe = Recipe.objects.filter(name__icontains = name).order_by('name')
            return recipe
        except Exception as error: 
            raise Exception(f'Error! - {error}')
                    
    def __str__(self) -> str:
        return f'Nome da receita = {self.name} - categoria = {self.category.name} - passos ={self.steps.all()}'


    