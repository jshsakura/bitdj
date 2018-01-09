from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^post_new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]