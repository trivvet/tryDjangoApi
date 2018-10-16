from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentCreateAPIView
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), 
        name='posts_list'),
    url(r'^create/$', CommentCreateAPIView.as_view(),
        name='post_create'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]