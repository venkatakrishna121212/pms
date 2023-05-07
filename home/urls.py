from django.urls import re_path
from student import views

app_name='home'
urlpatterns = [
    # home/ or /
    re_path(r'^$', views.studentlogin, name='home'),
    re_path(r'^home/', views.studentlogin, name='home'),
]
