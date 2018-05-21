from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.logreg),
    url(r'^process_reg$', views.processReg),
    url(r'^process_log$', views.processLog),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]