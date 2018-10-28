from django.conf.urls import url
from .views import (
    AccountListAPIView,
    AccountCreateAPIView,
    AccountLoginAPIView
    )

urlpatterns = [
    url(r'^$', AccountListAPIView.as_view(), name='list'),
    url(r'^create/$', AccountCreateAPIView.as_view(), name='register'),
    url(r'^login/$', AccountLoginAPIView.as_view(), name='login')
]