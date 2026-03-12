from django.urls import path
from .views import recipe_list, recipe, recipe_add, recipe_add_image

urlpatterns = [
    path('recipes/list/', recipe_list, name = 'recipe_list'),
    path('recipe/<str:name>', recipe, name = 'recipe'),
    path('recipe/add/', recipe_add, name = 'recipe_add'),
    path('recipe/<int:pk>/add_image/', recipe_add_image, name='recipe_add_image'),
]

app_name = "ledger"