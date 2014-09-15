from django.conf.urls import patterns, include, url
from school import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'index/', views.index),
    url(r'teacher$', views.teacher_panel, name="school_t_panel"),
    url(r'student', views.student_panel, name="school_s_panel"),
    url(r'teacher/register', views.create_student, name="school_register")
)
