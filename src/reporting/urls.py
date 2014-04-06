from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'reporting.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
