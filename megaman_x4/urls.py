"""
URL configuration for megaman_x4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp.views.home import index
from myapp.views.historia import historia
from myapp.views.itens import itens
from myapp.views.chefes import get_all_chefes
urlpatterns = [

    path('', index , name = 'home'),
    path('/historia', historia , name = 'historia'),
    path('/itens', itens , name = 'itens'),
    path('/chefes', get_all_chefes , name = 'chefes'),
]
