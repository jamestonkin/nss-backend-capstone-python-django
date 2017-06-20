# Creates fake voting data for testing until voting data can be scraped
import factory
from website.models import *

class BillVotingFactoryA(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake bill voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = BillVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=37)
    bill_legislation_synopsis = factory.Iterator(BillLegislationSynopsis.objects.all())

class ResolutionVotingFactoryA(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake resolution voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = ResolutionVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=37)
    resolution_legislation_synopsis = factory.Iterator(ResolutionLegislationSynopsis.objects.all())

class BillVotingFactoryB(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake bill voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = BillVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=38)
    bill_legislation_synopsis = factory.Iterator(BillLegislationSynopsis.objects.all())

class ResolutionVotingFactoryB(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake resolution voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = ResolutionVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=38)
    resolution_legislation_synopsis = factory.Iterator(ResolutionLegislationSynopsis.objects.all())

class BillVotingFactoryC(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake bill voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = BillVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=39)
    bill_legislation_synopsis = factory.Iterator(BillLegislationSynopsis.objects.all())

class ResolutionVotingFactoryC(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake resolution voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = ResolutionVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=39)
    resolution_legislation_synopsis = factory.Iterator(ResolutionLegislationSynopsis.objects.all())

class BillVotingFactoryD(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake bill voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = BillVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=40)
    bill_legislation_synopsis = factory.Iterator(BillLegislationSynopsis.objects.all())

class ResolutionVotingFactoryD(factory.django.DjangoModelFactory):
    """
    Class designed for creating fake resolution voting data within database
    Methods: N/A
    Author: James Tonkin
    Args: models.Model
    Returns: N/A
    """
    class Meta:
        model = ResolutionVoting
    vote = factory.Faker('random_int', min=0, max=3)
    council_member = CouncilMember.objects.get(pk=40)
    resolution_legislation_synopsis = factory.Iterator(ResolutionLegislationSynopsis.objects.all())
