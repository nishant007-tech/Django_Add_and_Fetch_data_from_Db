from Tools.scripts.which import msg
from django.shortcuts import render
from .models import Contact
from django import forms
from django.http import HttpResponse
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['msg']
        cont = Contact(name=name, email=email, phone=phone, content=content)
        cont.save()
    return render(request, 'templates/contact.html')

def home(request):
    obj = Contact.objects.all()
    return render(request, 'templates/index.html', {'obj': obj})
