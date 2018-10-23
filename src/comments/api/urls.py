from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentEditAPIView
    # CommentChildListAPIView
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), 
        name='comments_list'),
    # url(r'^(?P<id>\d+)/children/$', CommentChildListAPIView.as_view(), 
    #     name='comments_child_list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), 
        name='comment_detail'),
    url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), 
        name='comment_edit'),
    url(r'^create/$', CommentCreateAPIView.as_view(),
        name='comment_create'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]