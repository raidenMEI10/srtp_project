"""djangolearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    url和函数的对应关系
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),

    #一访问就执行这个函数
    path('index/', views.index),
    path('userlist/', views.userlist),
    path('something/',views.something),
    path('login/', views.login),
    path('createuser/', views.createuser),
    path('queryuser/', views.queryuser),
    path('predictfault/', views.predict_fault),
    path('predictsequence/', views.predict_sequence),
]
