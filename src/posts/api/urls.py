from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListApi,
    PostDetailAPIView,
    PostUpdateApiView,
    PostDeleteApiView,
    PostCreateApiView

	)

urlpatterns = [
	url(r'^$', PostListApi.as_view(), name='list-api'),
    url(r'^create/$',PostCreateApiView.as_view(),name="create"),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateApiView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteApiView.as_view(), name='delete'),
]
