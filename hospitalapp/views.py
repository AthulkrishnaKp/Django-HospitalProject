from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospitalapp.forms import BookingForm
from hospitalapp.models import Departments,Doctors

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')   
    form = BookingForm()
    return render(request,'booking.html',{'form':form})    

def doctors(request):
    doc=Doctors.objects.all()
    return render(request,'doctors.html',{'form':doc})  

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dept=Departments.objects.all()
    return render(request,'department.html',{'form':dept})    
