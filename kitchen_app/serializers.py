from rest_framework import serializers
from kitchen_app.models import Food, Category, Recipe,Step

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'more_info']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class StepSerializer(serializers.ModelSerializer):
    # ingredients = StepSerializer(many= True, read_only=True)
    class Meta:
        model = Step
        fields = ['description','number_step']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = FoodSerializer(many= True, read_only=True)
    steps = StepSerializer(many= True, read_only=True)
    class Meta:
        model = Recipe
        fields = ['name', 'category','image', 'ingredients', 'steps']

