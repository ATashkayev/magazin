"""magazin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
from instructor.views import home, clothes, list_instructor, instructor_id
from django.conf import settings
from products.views import *

print(url)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^index/', home),
    url(r'^index_clothes/', clothes),
    url(r'^checkout/$', chek_out, name="chek_out"),
    url(r'^basket/$', basket_adding, name="basketadding"),
    url(r'^product/(?P<product_id>\w+)/$', product_, name="productid"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
