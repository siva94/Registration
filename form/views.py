from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import Details
# Create your views here.


def index(request):
    return render(request, 'form/index.html')


def signup(request):
    return render(request, 'form/signup.html')


def details(request):
    nam=request.POST['name']
    ag=request.POST['age']
    mail=request.POST['email']
    locate=request.POST['location']
    res=Details(name=nam,age=ag,email=mail,location=locate)
    res.save()
    list_of_users=get_list_or_404(Details)
    return render(request,'form/details.html',{'users': list_of_users,'name': nam,'age': ag,'email': mail,'location': locate})