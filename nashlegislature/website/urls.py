from django.conf.urls import url

from website.views.views import *
from website.views.council_view import council_list
from website.views.bills_view import bill_list
from website.views.resolutions_view import resolution_list
from website.views.billvoting_view import bill_voting
from website.views.resovoting_view import resolution_voting
from website.views.search_view import legislation_search

app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^council$', council_list, name='council'),
    url(r'^council$', council_list, name='council'),
    url(r'^bills$', bill_list, name='bills'),
    url(r'^resolutions$', resolution_list, name='resolutions'),
    url(r'^bill_voting/(?P<billlegislationsynopsis_id>.+?)/$', bill_voting, name='bill_voting'),
    url(r'^resolution_voting/(?P<resolutionlegislationsynopsis_id>.+?)/$', resolution_voting, name='resolution_voting'),
    url(r'^legislation_search$', legislation_search, name='legislation_search'),
]
