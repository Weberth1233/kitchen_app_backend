from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from kitchen_app.models import Food, Category, Recipe, Step
from kitchen_app.serializers import FoodSerializer, CategorySerializer, RecipeSerializer, StepSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# Create your views here.

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_foods(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)  
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_categorys(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_recipe_by_steps(request, pk):
    if request.method == 'GET':
        recipe = Recipe.objects.get(pk=pk)
        steps = recipe.get_ordered_steps()
        serializer = StepSerializer(steps, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_recipe_by_category(request, pk):
    if request.method == 'GET':
        #Obtendo todos as receitas passando uma determinada categoria
        recipes = Recipe.get_recipes_by_category(pk)
        serializer = RecipeSerializer(recipes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_steps(request):
    if request.method == 'GET':
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

