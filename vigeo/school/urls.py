from django.conf.urls import patterns, include, url
from school import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'index/', views.index, name="school_index"),
    url(r'teacher$', views.teacher_panel, name="school_t_panel"),
    url(r'student', views.student_panel, name="school_s_panel"),
    url(r'teacher/register', views.create_student, name="school_register"),
    url(r'teacher/add_lesson', views.add_lesson, name="school_lesson"),
    url(r'teacher/add_category', views.add_category, name="school_category"),
    url(r'teacher/add_question', views.add_question, name="school_question"),
)
