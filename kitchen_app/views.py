from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from kitchen_app.models import Food, Category, Recipe, Step
from kitchen_app.serializers import FoodSerializer, CategorySerializer, RecipeSerializer, StepSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.core.paginator import Paginator
# Create your views here.

#---------------------------------Foods -------------------------------------------------------------
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_foods(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)  
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#--------------------------------- Categorys -------------------------------------------------------------
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_categorys(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#---------------------------------Recipes -------------------------------------------------------------
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_recipes_by_name(request):
    try:
        if request.method == 'POST':
            name = request.data.get("name")
            page_number = request.data.get("page")
            recipes = Recipe.filter_recipes_by_name(name=name)
            page_obj = Recipe.pagination(page_number=page_number, list=recipes)
            serializer = RecipeSerializer(page_obj, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_request": "Requisição incorreta - Use o método POST."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as error: 
            raise Exception(f'Error! - {error}')

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def fetch_recipe_pagination(request):
    if request.method == 'POST':
        recipes = Recipe.objects.all().order_by('id')
        page_obj = Recipe.pagination(page_number=request.data.get("page"), list=recipes)
        serializer = RecipeSerializer(page_obj, many = True)
        return Response(serializer.data)
    return Response({"error_request": "Requisição incorreta - Use o método POST."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def fetch_recently_recipe_pagination(request):
    recipes = Recipe.recently_recipes()
    page_obj = Recipe.pagination(page_number=request.data.get("page"), list=recipes)
    serializer = RecipeSerializer(page_obj, many = True)
    return Response(serializer.data)

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

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_recipes_by_filter_categorys(request):
    if request.method == 'POST':
        categorys = request.data.get("categorys")
        recipes_filter = Recipe.get_recipes_by_filter_categorys(categorys)
        serializer = RecipeSerializer(recipes_filter, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#-------------------------------Steps -------------------------------------
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fetch_steps(request):
    if request.method == 'GET':
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error_request": "Requisição incorreta - Use o método GET."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

