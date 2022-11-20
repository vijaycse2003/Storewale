from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime
from .models import *

# Create your views here.

def Error404(request,exception):
    return render(request,"./error404.html")

def ModalStore(request):
    cate=Category.objects.all()
    return render(request,'./Content/Modal.html',{"products":cate})  

def HomePage(request):
    company=Company.objects.all()
    return render(request,'./Content/biker.html',{"company":company })

def Bikers(request):
    vehicle=Vehicles.objects.filter(trending=1)
    return render(request,'./Content/bikers.html',{"products":vehicle})

def Combikes(request,coname):
     vechi=Vehicles.objects.filter(trending=1,vendor=coname)
     return render(request,'./Content/combikes.html',{"products":vechi})



def Details(request,cname,pname):
      if(Category.objects.filter(name=cname,status=1)):
        if(Vehicles.objects.filter(name=pname,status=0)):
             products=Vehicles.objects.filter(name=pname,status=0).first()
             Priced=products.price +20000
             timing=datetime.now()
             timing=timing.strftime("%B %d, %Y  %H:%M:%S")
            
             print(f"The time is ------ >{timing}")  
             return render(request,'./Content/showbike.html',{"products":products,"price":Priced,"stime":timing})
    
        else:
            messages.error(request,"No Such Category Found")
            return redirect('bikes')

      else:
        messages.error(request,"No Such Category Found")
        return redirect('home')
    