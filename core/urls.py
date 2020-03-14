"""simplemooc URL Configuration

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
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pages.views import home_view,contacts_view,socials_view,about_view	
from products.views import product_detail_view,product_create_view,dynamic_lookup_view,product_delete_view,product_list_view

urlpatterns = [
	path('',home_view,name='home'),
	path('contacts',contacts_view,name='contacts'),
	path('socials',socials_view,name='socials'),
	path('about',about_view,name='about'),
    path('create',product_create_view,name='product_create_view'),
    path('products/',product_list_view,name='product-list'),
	path('products/<int:id>/',dynamic_lookup_view,name='product-detail'),
    path('products/<int:id>/delete/',product_delete_view,name='product-delete'),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
