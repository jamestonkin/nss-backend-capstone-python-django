from django.shortcuts import render
from website.models import ResolutionLegislationSynopsis, ResolutionVoting


def resolution_voting(request, resolutionlegislationsynopsis_id):
    """
    purpose: gets the resolution voting data and displays on resovoting.html.
    author: James Tonkin
    args: request allows Django to see session data
    returns: Combines resovoting.html with resolution voting dictionaries and returns
    the request with that rendered text.
    """
    template_name = 'resovoting.html'
    current_resolution = ResolutionLegislationSynopsis.objects.get(pk=resolutionlegislationsynopsis_id)

    yes_votes = ResolutionVoting.objects.all().filter(
        resolution_legislation_synopsis_id=resolutionlegislationsynopsis_id, 
        vote=1
    )

    no_votes = ResolutionVoting.objects.all().filter(
        resolution_legislation_synopsis_id=resolutionlegislationsynopsis_id, 
        vote=0
    )

    abstain_votes = ResolutionVoting.objects.all().filter(
        resolution_legislation_synopsis_id=resolutionlegislationsynopsis_id, 
        vote=2
    )

    absent_votes = ResolutionVoting.objects.all().filter(
        resolution_legislation_synopsis_id=resolutionlegislationsynopsis_id, 
        vote=3
    )

    total_votes = ResolutionVoting.objects.all().filter(
        resolution_legislation_synopsis_id=resolutionlegislationsynopsis_id).count()

    return render(request, template_name,
        {'current_resolution': current_resolution,
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'abstain_votes': abstain_votes,
        'absent_votes': absent_votes,
        'total_votes': total_votes}
    )
