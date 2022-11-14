from django.shortcuts import render
from datetime import datetime
from user.models import Contact

# Create your views here.
def index(request):
    return render (request, 'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render (request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render (request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _desc = request.POST.get('desc')
        print(">>>>>>>>>>>>>>>>>>>>",_name, _email, _phone, _desc)
        
        contact1 = Contact(name=_name,email=_email, phone=_phone, desc="_desc", date= datetime.today())
        print(">>>>", type(contact1), "\n", dir(contact1))
        contact1.save()
     
     
     
    return render (request, 'Contact.html')
    # return HttpResponse("this is contact page")