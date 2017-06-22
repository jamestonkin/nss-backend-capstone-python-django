from django.shortcuts import render
from website.models import BillLegislationSynopsis, BillVoting


def bill_voting(request, billlegislationsynopsis_id):
    """
    purpose: gets the bill voting data and displays on billvoting.html.
    author: James Tonkin
    args: request allows Django to see session data
    returns: Combines billvoting.html with voting dictionaries and returns
    the request with that rendered text.
    """
    template_name = 'billvoting.html'
    current_bill = BillLegislationSynopsis.objects.get(pk=billlegislationsynopsis_id)

    yes_votes = BillVoting.objects.all().filter(
        bill_legislation_synopsis_id=billlegislationsynopsis_id, 
        vote=1
    )

    no_votes = BillVoting.objects.all().filter(
        bill_legislation_synopsis_id=billlegislationsynopsis_id, 
        vote=0
    )

    abstain_votes = BillVoting.objects.all().filter(
        bill_legislation_synopsis_id=billlegislationsynopsis_id, 
        vote=2
    )

    absent_votes = BillVoting.objects.all().filter(
        bill_legislation_synopsis_id=billlegislationsynopsis_id, 
        vote=3
    )

    total_votes = BillVoting.objects.all().filter(
        bill_legislation_synopsis_id=billlegislationsynopsis_id).count()

    return render(request, template_name,
        {'current_bill': current_bill,
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'abstain_votes': abstain_votes,
        'absent_votes': absent_votes,
        'total_votes': total_votes}
    )
