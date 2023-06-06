from django.db import models as recipe_store
# Create your models here.


class recipe_storage(recipe_store.Model):
    recipe_name = recipe_store.CharField(max_length=50)
    recipe_description = recipe_store.TextField()
    recipe_image = recipe_store.ImageField(upload_to="recipe_images")
