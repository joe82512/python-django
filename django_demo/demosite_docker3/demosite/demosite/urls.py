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
from demo2.views import info_demo, table_info, table_list, table_create
#from demo2.views import login
from demo2.views import login_forms, logout, signup, verification
#from django.urls import include
from django.contrib.auth import views
from demo2.views import NewPasswordResetView
from demo2.views import food, search_food, related_food
from demo2.views import data_page, data_ajax, count_ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    # demo1
    path('demo/', post, name='demo_url'),
    # demo2
    path('info/demo/', info_demo, name='info_demo_url'),
    path('info/<int:pk>/', table_info, name='info_url'),
    path('list/', table_list, name='list_url'),
    path('create/', table_create, name='create_url'),
    # login / logout
    #path('', login, name='login'),
    path('', login_forms, name='login'),
    path('logout/', logout, name='logout'),
    
    # Sign up
    path('signup/', signup, name='signup'),
    path('verification/', verification, name='verification'),

    # accounts
    #path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', NewPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    ### advance ###
    path('food/', food, name='food'),
    path('food/search', search_food, name='search_food'),
    path('food/related', related_food, name='related_food'),

    ### ajax ###
    path('food/ajax/', data_page, name='data_page'),
    path('data_ajax', data_ajax, name='data_ajax'),
    path('count_ajax', count_ajax, name='count_ajax')
]

# debug
from django.conf import settings
from django.urls import include
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns