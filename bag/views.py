from django.shortcuts import render


def view_bag(request):
    """ A view to render's the shopping bad"""
    return render(request, 'bag/bag.html')
