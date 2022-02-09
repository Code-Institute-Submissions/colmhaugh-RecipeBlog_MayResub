from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

COURCE_CHOICE = [(0, 'Starter'), (1, 'Soup'),(2, 'Main'), (3, 'Dessert')]
STATUS = ((0, 'Draft'), (1, 'Published'))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_post")
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    cource = models.IntegerField(choices=COURCE_CHOICE)
    likes = models.ManyToManyField(User, related_name='recipepost_like', blank=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe(), on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.name}"