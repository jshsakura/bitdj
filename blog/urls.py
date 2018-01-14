from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^post_new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)