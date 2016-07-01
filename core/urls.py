from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from core import views

requester_patterns = [
  url(r'^$', views.RequesterList.as_view(), name='requester_list'), #core home
  url(r'^requesters$', views.RequesterList.as_view(), name='requester_list'),
  url(r'^new_requester$', views.RequesterCreate.as_view(), name='requester_create'),
  url(r'^edit_requester/(?P<pk>\d+)$', views.RequesterUpdate.as_view(), name='requester_update'),
  url(r'^delete_requester/(?P<pk>\d+)$', views.RequesterDelete.as_view(), name='requester_delete'),
]

consultant_patterns = [
  url(r'^$', views.ConsultantList.as_view(), name='consultant_list'),
  url(r'^consultants$', views.ConsultantList.as_view(), name='consultant_list'),
  url(r'^new_consultant$', views.ConsultantCreate.as_view(), name='consultant_create'),
  url(r'^edit_consultant/(?P<pk>\d+)$', views.ConsultantUpdate.as_view(), name='consultant_update'),
  url(r'^delete_consultant/(?P<pk>\d+)$', views.ConsultantDelete.as_view(), name='consultant_delete'),
]

request_patterns = [
  url(r'^$', views.RequestList.as_view(), name='request_list'),
  url(r'^requests$', views.RequestList.as_view(), name='request_list'),
  url(r'^new_request$', views.RequestCreate.as_view(), name='request_create'),
  url(r'^edit_request/(?P<pk>\d+)$', views.RequestUpdate.as_view(), name='request_update'),
  url(r'^delete_request/(?P<pk>\d+)$', views.RequestDelete.as_view(), name='request_delete'),
]

tag_patterns = [
  url(r'^$', views.TagList.as_view(), name='tag_list'),
  url(r'^tags$', views.TagList.as_view(), name='tag_list'),
  url(r'^new_tag$', views.TagCreate.as_view(), name='tag_create'),
  url(r'^edit_tag/(?P<pk>\d+)$', views.TagUpdate.as_view(), name='tag_update'),
  url(r'^delete_tag/(?P<pk>\d+)$', views.TagDelete.as_view(), name='tag_delete'),
]

#any pattern included on the file must be imported here
urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name='homepage.html'),name='homepage'),
  url(r'^requesters/',include(requester_patterns)),
  url(r'^consultants/',include(consultant_patterns)),
  url(r'^requests/',include(request_patterns)),
  url(r'^tags/',include(tag_patterns)),
  
)
