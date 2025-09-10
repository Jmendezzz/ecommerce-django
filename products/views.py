from django.shortcuts import render
from .models import Category

# Views define the html file and gives the data.

def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})