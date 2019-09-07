"""basic_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    """ this url using for create new user """
    path('u-create/',views.UserCreateGenericAPI.as_view(),name="user-create"),

    """ this url using to update existing user """
    path('u-update/<int:id>/',views.UserUpdateGenericAPI.as_view(),name="user-update"),

    """ this url using to add user profile"""
    path('u-pro-create/',views.UserUpdateGenericAPI.as_view(),name="user-update"),

    """ this url using to authenticate user with username or password""",
    path('u-login/',views.LoginApiView.as_view(),name="user-login"),

    """ this url using for default api-authentication"""
    path('api-auth/',include('rest_framework.urls',namespace="rest_framework")),
]
