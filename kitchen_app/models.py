from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'Nome da comida = {self.name} - informações adicionais = {self.info}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Nome da categoria = {self.name}'

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self) -> str:
        return f'Nome da receita = {self.title} - categoria = {self.category.name}'

class Steps(models.Model):
    description = models.CharField(max_length=200)
    number_step = models.IntegerField()
    recipe_fk = models.ForeignKey(Recipe,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Nome da receita = {self.recipe_fk.title} - description = {self.description} - etapa = {self.number_step}'
 
class RecipeIngredients(models.Model):
    recipe_fk = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_fk = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Nome da receita = {self.recipe_fk.title} - comida = {self.food_fk.name}'
