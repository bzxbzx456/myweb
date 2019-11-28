from django.urls import path

from users.views import index, test, tag_demo, template_extends, include_demo, login

urlpatterns = [
    path('',index),
    path('test',test),
    path('tag',tag_demo),
    path('temp',template_extends),
    path('include',include_demo),
    path('login',login,name='login')
]