from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from subApp.models import hiring
# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        date=request.POST['date']
        telephone=request.POST['telephone']
        address=request.POST['address']
        experience=request.POST['experience']
        position=request.POST['position']
        resume=request.FILES['resume']
        print(resume.name)
        print(resume.size)
        obj=hiring(name=name,email=email,dob=date,telphone=telephone,Add=address,totalExp=experience,position=position,portfolio=resume)
        obj.save()
        messages.success(request,"We will contact ASAP")
        # return HttpResponse('form sent.')
            
            
    return render(request,'contact.html')
