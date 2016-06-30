from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^$', views.RequesterList.as_view(), name='requester_list'), #core home
  url(r'^requesters$', views.RequesterList.as_view(), name='requester_list'),
  url(r'^new_requester$', views.RequesterCreate.as_view(), name='requester_create'),
  url(r'^edit_requester/(?P<pk>\d+)$', views.RequesterUpdate.as_view(), name='requester_update'),
  url(r'^delete_requester/(?P<pk>\d+)$', views.RequesterDelete.as_view(), name='requester_delete'),
)
