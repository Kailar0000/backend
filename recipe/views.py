from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest


from .models import Recipes
from .forms import RecipeForm


def recipes_list(request):
    random_recipes = Recipes.objects.order_by('?')[:5]
    return render(request,'recipe/recipes_list.html',{'random_recipes':random_recipes})

def recipe_page(request: HttpRequest, recipe_pk):
    recipe = get_object_or_404(Recipes, pk=recipe_pk)
    return render(request, 'recipe/recipe_page.html', context={'recipe':recipe})

def new_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return recipe_page(request, recipe.pk)
        else:
            return render(request, 'recipe/new_recipe.html', {'form': form})
    return render(request, 'recipe/new_recipe.html', {'form': RecipeForm()})

def update_recipe(request, recipe_pk):
    if request.method == "POST":
        instance = get_object_or_404(Recipes, pk=recipe_pk)
        form = RecipeForm(request.POST or None, instance=instance)
        if form.is_valid():
            recipe = form.save()
            return recipe_page(request, recipe.pk)
        else:
            return render(request, 'recipe/new_recipe.html', {'form': form})
    return render(request, 'recipe/new_recipe.html', {'form': RecipeForm()})
