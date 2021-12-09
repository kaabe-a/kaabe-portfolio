from django.urls import path
from . views import post_list,post_detail,post_create,post_update,post_delete
urlpatterns = [
    path('',post_list,name='home'),
    path('detail/<str:pk>/',post_detail,name='detail'),
    path('update/<str:pk>/',post_update,name='update'),
    path('delete/<str:pk>/',post_delete,name='delete'),
    path('create/',post_create,name='create'),

]