from django.conf.urls import patterns, include, url
from compass import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^enquiry/$', views.enquiry),
    url(r'^about/$', views.about),
    url(r'^service/$', views.services),
    url(r'^careers/$', views.career),
    url(r'^contact/$', views.message),
    url(r'^vessel/$', views.vessel),
    url(r'^custom/$', views.custom),
    url(r'^transport/$', views.transport),
    url(r'^freight/$', views.freight),
    url(r'^picorrespondents/$', views.pi),
    url(r'^ship/$', views.ship),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(?P<reference_no>\S+)/$', views.status),
    
)
