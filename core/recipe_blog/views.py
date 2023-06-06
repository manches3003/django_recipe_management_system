from django.shortcuts import render
from .models import *

# Create your views here.


def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        # return redirect("/recipes/")

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        recipe_storage.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

    queryset = recipe_storage.objects.all()
    context = {' recipes ': queryset}

    return render(request, 'recipe.html', context=context)
