from django.shortcuts import render
from website.models import ResolutionLegislationSynopsis


def resolution_list(request):
    """
    purpose: gets all resolutions to be viewed on resolutions.html
    author: James Tonkin
    args: request allows Django to see user session data
    returns: Combines resolutions.html with resolution_list dictionary and returns
    the request with that rendered text.
    """
    template_name = 'resolutions.html'
    resolution_list = ResolutionLegislationSynopsis.objects.all().order_by('id')
    return render(request, template_name, {'resolution_list': resolution_list})
