"""
URLs for the project my recipes
app.  Mostly of detail and list
views
"""

from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('starter/', views.StarterList.as_view(), name='starter'),
    path('soup/', views.SoupList.as_view(), name='soup'),
    path('main/', views.MainList.as_view(), name='main'),
    path('dessert/', views.DessertList.as_view(), name='dessert'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('comment/edit/<int:id>/', views.EditComment.as_view(), name='comment_edit'),
    path('comment/delete/<int:id>/', views.DeleteComment.as_view(), name='comment_delete'),
    
]
