from django.conf.urls import url

from shortener.views import follow

urlpatterns = (
    # url(r'^$', 'index', name='index'),
    # url(r'^info/(?P<short_url>.*)$', 'info', name='info'),
    # url(r'^submit/$', 'submit', name='submit'),
    # url(r'^link_access_map/$', 'access_map', name='map_access'),
    url(r'^(?P<base62_id>.*)$', follow, name='shortener.views.follow'),
)
