from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("logout", views.logout_request, name= "logout"),  
     path('client_list/', views.client_list, name='client_list'),
]