from rest_framework import serializers
from kitchen_app.models import Food, Category, Recipe,Step

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'more_info']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class StepSerializer(serializers.ModelSerializer):
    # ingredients = StepSerializer(many= True, read_only=True)
    class Meta:
        model = Step
        fields = ['description','number_step']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = FoodSerializer(many= True, read_only=True)
    steps = StepSerializer(many= True, read_only=True)
    category = CategorySerializer()

    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'category','image_url','time_to_prepare', 'ingredients', 'steps','created_at']
    
    def get_image_url(self, obj):
        return obj.image.url if obj.image else None

