from django.shortcuts import render

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from instructor.models import Instructors

# Create your views here.


def home(request):
    #print(request.path)
    #print(request.GET['d'])
    return render(request,"index.html")	

def clothes(request):
    return render(request,"index_clothes.html")

def list_instructor(request):
	 #print(request.path)
	instructor = Instructors.objects.all()
	return render(request,"list_instructors.html",{"instructors":instructor})


def instructor_id(request, id):
	print(id)
	instructor = Instructors.objects.filter(id=id)
	return render(request,"instructor_id.html",{"instructor":instructor})
    
