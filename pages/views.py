from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	return render(request,"home.html",{})
# Create your views here.
def contacts_view(request,*args,**kwargs):
	return render(request,"contacts.html",{})

def socials_view(request,*args,**kwargs):
	return render(request,"social.html",{})

def about_view(request,*args,**kwargs):
	my_context={
	"my_text":"This is about us ",
	"this_is_true":True,
	"my_number": 123,
	"my_list":[123,234,456]
	}

	return render(request,"about.html",my_context)	