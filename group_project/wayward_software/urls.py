from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sign_up/', views.sign_up, name='sign_up'),  
    path('login/', views.login, name='login'), 
]