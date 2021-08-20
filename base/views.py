from django.shortcuts import render
from.forms import Contactform
from .models import Contactmessage
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
	if request.method =="POST":
		form = Contactform(request.POST)
		if form.is_valid():
			fullname = form.cleaned_data.get('fullname')
			email = form.cleaned_data.get('email')
			subject = form.cleaned_data.get('subject')
			gender = form.cleaned_data.get('gender')
			message =form.cleaned_data.get('body')
			messages.success(request,f'Message Sent')
			new_message = Contactmessage.objects.create(fullname=fullname,email=email,subject=subject,gender=gender,message=message)
			new_message.save()
		
	else:
    		form = Contactform()
	
	return render(request,'base/home.html',{'form':form})
    		
