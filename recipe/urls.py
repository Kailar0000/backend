from django.urls import path
from .views import recipes_list, recipe_page, new_recipe, update_recipe



urlpatterns = [
    path('', recipes_list, name='home'),
    path('recipe/<int:recipe_pk>/', recipe_page, name='recipe_detail'),
    path('newrecipe', new_recipe, name='new_recipe'),
    path('updaterecipe', update_recipe, name='new_recipe'),
]