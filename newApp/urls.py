from django.urls import path
from newApp import views


# Name for the urls path
app_name = 'newApp'

# Defining the paths for the App
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user_page, name='user'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name="user_logout")
]
