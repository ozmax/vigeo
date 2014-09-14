from django.conf.urls import patterns, include, url
from school import views

urlpatterns = patterns('',
    url(r'^$', views.login_view),
    url(r'^logout', views.logout_view),
    url(r'^dec', views.test_dec),
)
