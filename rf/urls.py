from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'registration.views.home', name='home'),
    url(r'^brackets/', 'registration.views.brackets', name='home'),
    url(r'^register/', 'registration.views.register', name='home'),
    (r'^staticfiles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_PREFIX, 'show_indexes': True}),
    (r'^admin/', include(admin.site.urls)),
)
