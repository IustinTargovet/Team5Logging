from django.conf.urls import url
from . import views

app_name = 'text'

urlpatterns = [

    url(r'^$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout-user'),

    url(r'^home/$', views.IndexView.as_view(), name = 'index'),

    url(r'^register/$', views.UserFormCreate.as_view(), name = 'register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    url(r'^log/add/$', views.create_log, name = 'log-add'),

    url(r'^log/(?P<pk>[0-9]+)/$', views.LogUpdate.as_view(), name = 'log-update'),

    url(r'^log/entry_view$', views.EntryView.as_view(), name = 'entry_view'),

    url(r'^log/(?P<pk>[0-9]+)/delete$', views.LogDelete.as_view(), name = 'log-delete'),

    url(r'^(?P<log_id>[0-9]+)/create_entry/$', views.create_entry, name='create_entry'),
]
