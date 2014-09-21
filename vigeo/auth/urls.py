from django.conf.urls import patterns, include, url
from auth import views

urlpatterns = patterns('',
    url(r'^$', views.login_view),
    url(r'^login/$', views.login_view, name="auth_login"),
    url(r'^logout/$', views.logout_view, name="auth_logout"),
)
