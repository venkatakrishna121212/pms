from django.urls import re_path
from . import views

app_name='company'

urlpatterns = [
    re_path(r'signup', views.post_list, name='signup_page'),
    re_path(r'login', views.view_home, name='login_page'),
    re_path(r'edit', views.view_edit, name='home_page'),
    re_path(r'verify', views.verify, name='verify_page'),
    re_path(r'userc/(?P<username>[A-Za-z_0-9]+)/$', views.profile, name='profile'),
    re_path(r'jobreqs', views.Jobreqs, name='job_requirements'),
    re_path(r'change_password', views.change_password, name='passchg'),
    re_path(r'changed', views.successfull_change, name='passchgsucc'),
    re_path(r'listjobs', views.listjobs, name='listjobs'),
    re_path(r'jobs/(?P<jobid>[0-9]+)/', views.jobdesc, name='jobdesc'),
    re_path(r'applied_msg/', views.jobapplied, name='jobapplied'),
    re_path(r'student_list/(?P<jobid>[0-9]+)/', views.view_student_list, name='studlist'),
    re_path(r'taken_name/', views.already_taken, name="takenc"),
    re_path(r'offered/(?P<userid>[A-Za-z_0-9]+)/$', views.offered, name="takenc"),
]

