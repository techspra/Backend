from django.conf.urls import include, url
from django.contrib import admin
from home.views import *
from contact.views import getForm
urlpatterns = [
    # Examples:
    # url(r'^$', 'brainjack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',GetHome),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$',GetAbout),
    url(r'^query/',getForm),
    url(r'^contact/$',GetContact),
    url(r'^gallery/$',GetGallery),
]
