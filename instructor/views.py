from django.shortcuts import render

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from instructor.models import Instructors
from products.models import Products
# Create your views here.


def home(request):


    products = Products.objects.filter(is_active = True)

    return render(request,"home.html", locals())

def clothes(request):
    return render(request,"home.html")

def list_instructor(request):
	 #print(request.path)
	instructor = Instructors.objects.all()
	return render(request,"list_instructors.html",{"instructors":instructor})


def instructor_id(request, id):
	print(id)
	instructor = Instructors.objects.filter(id=id)
	return render(request,"instructor_id.html",{"instructor":instructor})
    
