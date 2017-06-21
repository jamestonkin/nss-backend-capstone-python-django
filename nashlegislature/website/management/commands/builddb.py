from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from website.factories import *

class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    the necessary shell commands to generate our database's tables and
    load our data to them via Faker. These commands are, in order:
    1. python manage.py makemigrations api
    2. python manage.py migrate
    3. (Factory Calls): Category, User, Payment, Product, ProductOrder
    Author: Adam Myers
    """

    def handle(self, *args, **options):
        management.call_command('makemigrations', 'website')
        management.call_command('migrate')
        # ResolutionVotingFactoryA.create_batch(size=765)
        # ResolutionVotingFactoryB.create_batch(size=765)
        # ResolutionVotingFactoryC.create_batch(size=765)
        # ResolutionVotingFactoryD.create_batch(size=765)
        # ResolutionVotingFactoryE.create_batch(size=765)
        BillVotingFactoryA.create_batch(size=796)
        BillVotingFactoryB.create_batch(size=796)
        BillVotingFactoryC.create_batch(size=796)
        # BillVotingFactoryD.create_batch(size=796)
        # BillVotingFactoryE.create_batch(size=796)
        # UserFactory.create_batch(size=5)
        """
        UserFactory is commented out due to the factory now being a one to one with the profile factory, profile factory calls upon the creation of the user through the profilefactory, line 175 in factories.py
        """
