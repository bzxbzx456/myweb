from django.urls import path
from app.views import index,index1,index2,index3
urlpatterns = [
    path('app',index),
    path('app1',index1),
    path('app2',index2),
    path('app3',index3),
]