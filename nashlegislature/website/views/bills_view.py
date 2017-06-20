from django.shortcuts import render
from website.models import BillLegislationSynopsis


def bill_list(request):
    """
    purpose: gets all bills to be viewed on bills.html
    author: James Tonkin
    args: request allows Django to see user session data
    returns: Combines bills.html with bill_list dictionary and returns
    the request with that rendered text.
    """
    template_name = 'bills.html'
    bill_list = BillLegislationSynopsis.objects.all().order_by('id')
    return render(request, template_name, {'bill_list': bill_list})
