from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("logout", views.logout_request, name= "logout"),  
]