from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('compass.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
