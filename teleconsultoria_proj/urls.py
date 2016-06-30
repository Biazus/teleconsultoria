from django.conf.urls import include, url
from django.contrib import admin
import core.urls

urlpatterns = [
    # Examples:
    #url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^c/', include(core.urls)),
    url(r'^core/', include('core.urls')),
]
