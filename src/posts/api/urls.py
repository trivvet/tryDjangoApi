from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[\w-]+)/$', PostDetailAPIView.as_view(), 
        name='post_detail'),
    url(r'^(?P<pk>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), 
        name='post_update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', PostDestroyAPIView.as_view(), 
        name='post_delete'),
   
]