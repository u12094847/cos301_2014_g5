
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'ReportsTwo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^assessments/', 'ReportsTwo.views.assessments',name='assessments'),
    #url(r'^admin/', include(admin.site.urls)),
    
)
