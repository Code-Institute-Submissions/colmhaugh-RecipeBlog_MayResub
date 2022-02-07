from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ('cource', 'status', 'created_on')
    summernote_fields = ('description', 'ingredients', 'instructions')
    list_display = ('title', 'slug', 'cource', 'status', 'created_on')
    actions = ['approve_recipe']

    def approve_recipe(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)