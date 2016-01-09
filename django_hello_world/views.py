from django.http import HttpResponse


def index(request):
    """
    Show welcome text on the index page
    """
    return HttpResponse('Hello world!')
