from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^add$', views.add),
    url(r'^process_trip$', views.processTrip),
    url(r'^join/(?P<id>\d+)$', views.join)
]
