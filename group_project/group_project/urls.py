"""group_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from wayward_software import views as w

urlpatterns = [
    path('admin/', admin.site.urls),
    #-S links to the views file in the register folder
    path("register/", v.register, name="register"),
    path('', include('wayward_software.urls')),
    #-S added this to show css on the site
    path("index/", w.index),
    path("sign_up", w.sign_up),
    path("login", w.login),

]