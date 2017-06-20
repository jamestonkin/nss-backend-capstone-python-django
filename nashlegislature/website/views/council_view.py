from django.shortcuts import render
from website.models import CouncilMember


def council_list(request):
    """
    purpose: gets all council members to be viewed on council.html
    author: James Tonkin
    args: request allows Django to see user session data
    returns: Combines council.html with council_members dictionary and returns
    the request with that rendered text.
    """
    template_name = 'council.html'
    council_members = CouncilMember.objects.all().order_by('id')
    return render(request, template_name, {'council_members': council_members})
