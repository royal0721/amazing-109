"""Amazing_109_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from cookieManager import views 
from django.conf.urls.static import static
from django.conf import settings
# router = routers.DefaultRouter()
# router.register(r'Product', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cookieManager.urls')),

    path('', views.login_form),
    path('crmPage/', views.crmPage),
    path('discountPage/', views.discountPage),
    path('inventoryPage/', views.inventoryPage),
    path('login_form/',views.login_form),
    path('logout/',views.logout),
    path('index/',views.index),
]