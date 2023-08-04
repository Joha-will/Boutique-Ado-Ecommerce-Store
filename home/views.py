from django.shortcuts import render


def index(request):
    """ A view to render index page"""
    return render(request, 'home/index.html')


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 """
    return render(request, "errors/500.html", status=500)