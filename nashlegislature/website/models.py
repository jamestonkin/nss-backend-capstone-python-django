from django.db import models

options = (
        (0, 'No'),
        (1, 'Yes'),
        (2, 'Abstain'),
        (3, 'Absent'),
)

class CouncilMember(models.Model):
    """
    Class designed for creating council members within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    first_name = models.CharField(max_length=54)
    last_name = models.CharField(max_length=54)
    email = models.EmailField(max_length=54)
    district = models.CharField(max_length=25)

class BillLegislationSynopsis(models.Model):
    """
    Class designed for creating bill legislation synopsis within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    link_to_bill = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254)
    synopsis = models.TextField(blank=True, null=True)

class ResolutionLegislationSynopsis(models.Model):
    """
    Class designed for creating resolution legislation synopsis within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    link_to_resolution = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254)
    synopsis = models.TextField(blank=True, null=True)

class BillVoting(models.Model):
    """
    Class designed for creating billvoting within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    bill_legislation_synopsis = models.ForeignKey(BillLegislationSynopsis)
    council_member = models.ForeignKey(CouncilMember)
    vote = models.IntegerField(default=0, choices=options)

class ResolutionVoting(models.Model):
    """
    Class designed for creating resolutionvoting within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    resolution_legislation_synopsis = models.ForeignKey(ResolutionLegislationSynopsis)
    council_member = models.ForeignKey(CouncilMember)
    vote = models.IntegerField(default=0, choices=options)



