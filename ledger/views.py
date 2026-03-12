from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, Ingredient, Profile, RecipeIngredient, RecipeImage

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipe_list.html", context)

@login_required
def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    context = {
        'recipe': recipe,
        'name': recipe.name,
        'ingredients': ingredients,
        'author': recipe.author.name,
        'images': recipe.images.all()}
    return render(request, "recipe.html", context)

def recipe_add(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()

            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()

    return render(request, "recipe_form.html", {"form": form})

@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            return redirect('ledger:recipe', name=recipe_image.recipe.name)
    else:
        form = RecipeImageForm()

    ctx = {"form": form, "recipe": recipe}
    return render(request, "add_image.html", ctx)