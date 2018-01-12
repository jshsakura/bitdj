from django.conf.urls import url
from django.urls import include

from account.views import UserCreateView, UserCreateDoneTemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTemplateView.as_view(), name='register_done'),
]