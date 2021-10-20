"""demosite URL Configuration

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
from django.urls import path
from demo1.views import post
from demo2.views import info_demo, table_info, table_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # demo1
    path('demo/', post, name='demo_url'),
    # demo2
    path('info/demo/', info_demo, name='info_demo_url'),
    path('info/<int:pk>/', table_info, name='info_url'),
    path('list/', table_list, name='list_url'),    
]
