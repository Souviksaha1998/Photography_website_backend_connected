from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from home.models import Contact , Images
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html');
def about(request):
    return render(request,'about.html');
def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        desc = request.POST.get('desc')
        if len(name)<4:
            messages.error(request," please Enter your name carefully")
        elif len(email)<5:
            messages.error(request," please Enter your email carefully")
        elif len(phone)<10:
            messages.error(request," please Enter your phone number carefully")   
        else:
            contact = Contact(name= name , email= email , phone=phone , desc=desc , date=datetime.today())
            contact.save()
            messages.success(request, 'Your form has been sent successfully')  
            
    return render(request,'contact.html',);
def explore(request):
    photo = Images.objects.all()
    context = {'photo' : photo}
    return render(request,'explore.html' , context);
