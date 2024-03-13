"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index
from .views import store_name
from .views import get_data
from .views import download_data

urlpatterns = [
    path("", index),
    path('store-name/', store_name, name='store_name'),
    path('documentation/downloads', download_data, name='download_documentation'),
    path('get-data/', get_data, name='get_data'),
    path('admin/', admin.site.urls),
]
