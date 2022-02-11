from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('starter/', views.StarterList.as_view(), name='starter'),
    path('soup/', views.SoupList.as_view(), name='soup'),
    path('main/', views.MainList.as_view(), name='main'),
    path('dessert/', views.DessertList.as_view(), name='dessert'),
    # path('addrecipes/', views.AddRecipe.as_view(), name='add_recipe'),
    # path('myrecipes/', views.MyRecipeList.as_view(), name='my_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
]
