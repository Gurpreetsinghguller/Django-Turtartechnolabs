from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Contact,Post
from django.contrib.auth.models import User 
from datetime import datetime

# Create your views here.

def index(request):
    obj =Post.objects.all()
    return render(request,'index.html',{'post':obj})




def about(request):
    return render(request,'about.html')


def skills(request):
    return render(request,'skills.html')


def contact(request):

    if request.method=='POST':
                name=request.POST.get('name')
                email=request.POST.get('email')
                number=request.POST.get('number')
                message=request.POST.get('message')
                log=Contact(name=name,email=email,mobile_no=number,date="",message=message)
                log.save()
                return render(request,'contact.html')
    return render(request,'contact.html')


def blog(request):
    obj =Post.objects.all()
    return render(request,'blog.html',{'post':obj})





def post(request,sno):
    obj1=get_object_or_404(Post,sno=sno)
    return render(request,'post.html',{'post':obj1})




