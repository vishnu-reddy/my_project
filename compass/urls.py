from django.conf.urls import patterns, include, url
from compass import views

urlpatterns = patterns('',
    url(r'^$', views.enquiry),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
)
