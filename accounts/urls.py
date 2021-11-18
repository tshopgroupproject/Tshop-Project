from django.conf.urls import url, include
from django.urls import path
from .views import register, profile, logout, login, reset, sendMail
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    path('logout/', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^reset/$', reset, name='reset'),
    path('', sendMail),


]
