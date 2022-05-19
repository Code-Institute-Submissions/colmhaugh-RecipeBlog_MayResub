from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm
from django.contrib import messages


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class StarterList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, cource=0).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class SoupList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, cource=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class MainList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, cource=2).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DessertList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, cource=3).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class EditComment(View):
    def get(self, request, id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=id) 
        recipe = get_object_or_404(Recipe, id=comment.recipe.id)        
        comment_form = CommentForm(instance=comment)
        return render(
            request,
            "comment_edit.html",
            {
                "recipe": recipe,
                "comment": comment,  
                "comment_form": comment_form,             
            },
        )

    def post(self, request, id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=id) 
        recipe = get_object_or_404(Recipe, id=comment.recipe.id)        
        comment_form = CommentForm(request.POST or None, instance=comment)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.success(request, "Comment update pending approval")
            
            return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.slug]))

        else:
            messages.error(request, "Error please try again")
                    
        return render(
            request,
            "comment_edit.html",
            {
                "recipe": recipe,
                "comment": comment,  
                "comment_form": comment_form,             
            },
        )


class DeleteComment(View):
    def get(self, request, id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=id) 
        recipe = get_object_or_404(Recipe, id=comment.recipe.id) 
        comment.delete()
        messages.success(request, "Comment deleted")
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.slug]))
