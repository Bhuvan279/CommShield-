from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addUser, name='add-user'),
    path('show/', views.showUsers, name='show-user'),
    path('location/<str:pk>/', views.showUsersInZip, name='show-user-in-zip'),

    path('victim-info/', views.showVictimsInfo, name='show-all-victims'),
    path('victim-post/', views.postVictimsInfo, name='post-victim-info'),
]
