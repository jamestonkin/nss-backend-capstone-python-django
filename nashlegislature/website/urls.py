from django.conf.urls import url

from website.views.views import *
from website.views.council_view import council_list
from website.views.bills_view import bill_list
from website.views.resolutions_view import resolution_list

app_name = "website"
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^council$', council_list, name='council'),
    url(r'^council$', council_list, name='council'),
    url(r'^bills$', bill_list, name='bills'),
    url(r'^resolutions$', resolution_list, name='resolutions'),
]
