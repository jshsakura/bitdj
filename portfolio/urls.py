from django.conf.urls import url
# from portfolio.views import create
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plex', views.plex, name='plex'),
    # url(r'^portfolio/upload/$', create, name='create'),
]