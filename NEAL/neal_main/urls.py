from django.conf.urls import patterns, url
from views import *
from django.conf import settings

urlpatterns = patterns('',
    # ex: /neal_main/
    url(r'^$', neal_index, name='neal_index'),
    url(r'^about/$', about, name='about'),
    url(r'^downloads/$', downloads, name='downloads'),
    url(r'^objects/$', objects, name='objects'),
    url(r'^objects/(?P<category>[\w\-]+)/$', objects_selected, name='objects_selected'),
    url(r'^objects/(?P<category>[\w\-]+)/(?P<object_name>[\w\-]+)$', category_objects_selected, name='category_objects_selected'),
    url(r'^segments/$', segments, name='segments'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

)
  
