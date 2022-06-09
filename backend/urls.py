from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('storage/', views.storage, name='storage'),
    path('storage/details/', views.details, name='details'),
    path('add_user/', views.addUser, name='add_user'),
    path('storage/register_file/', views.register_file, name='register_file'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2')
]
