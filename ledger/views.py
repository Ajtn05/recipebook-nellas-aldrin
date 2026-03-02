from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipe_list.html", context)

@login_required
def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    context = {'name': str(recipe), 'ingredients': ingredients, 'author': recipe.author.name}
    return render(request, "recipe.html", context)