from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view that renders all products"""

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
