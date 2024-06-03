from django.http import HttpResponse
from django.shortcuts import render

from .models import candidate

# Create your views here.
def welcome(request):
     return render(request,'welcome.html')
def home(request):
     return render(request,'index.html')
    
def form(request):
     if request.method=='POST':
        un=request.POST['username']  
        m=request.POST['email']
        p=request.POST['phone']
        obj=candidate(User_name=un,email_id=m,phone=p)  
        obj.save()
     return render(request,'index.html')