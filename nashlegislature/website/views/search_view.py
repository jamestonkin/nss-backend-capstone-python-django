from django.shortcuts import render
from django.db.models import Q
from website.models import BillLegislationSynopsis, ResolutionLegislationSynopsis

def legislation_search(request):
    """
    purpose: allows a user to search all legislation in the database
    author: James Tonkin
    args: gets all bills and resolutions, then filters by query (q)
    returns: a filtered list of legislation that match the query rendered on search.html
    """

    all_bills = BillLegislationSynopsis.objects.all().order_by("name", "synopsis")
    all_resolutions = ResolutionLegislationSynopsis.objects.all().order_by("name", "synopsis")
    query = request.GET.get("q")
    template_name = 'search.html'
    if query:   
        bills = all_bills.filter(Q(name__contains=query) | Q(synopsis__contains=query)).distinct()
        resolutions = all_resolutions.filter(Q(name__contains=query) | Q(synopsis__contains=query)).distinct()
        return render(request, template_name, {'all_bills': bills, 'all_resolutions': resolutions})
