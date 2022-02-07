from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ('cource', 'status', 'created_on')
    summernote_fields = ('description', 'ingredients', 'instructions')
    list_display = ('title', 'slug', 'cource', 'status', 'created_on')
