from django.shortcuts import render


def index(request):
    """
    purpose: Renders the home page
    author: James Tonkin
    args: request allows Django to see user session data
    returns: Renders the index.html (home page)
    """
    template_name = 'index.html'
    return render(request, template_name)


