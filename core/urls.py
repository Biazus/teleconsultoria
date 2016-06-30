from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^$', views.RequesterList.as_view(), name='requester_list'),
  url(r'^new$', views.RequesterCreate.as_view(), name='requester_new'),
  url(r'^edit/(?P<pk>\d+)$', views.RequesterUpdate.as_view(), name='requester_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.RequesterDelete.as_view(), name='requester_delete'),
)
