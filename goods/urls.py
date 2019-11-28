from django.urls import path

from goods.views import all_goods, add_goods, delete_goods, update_goods

urlpatterns = [
    path('all',all_goods),
    path('add',add_goods),
    path('delete',delete_goods),
    path('update/<str:name>',update_goods)
]