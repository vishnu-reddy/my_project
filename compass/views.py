from django.shortcuts import render ,render_to_response, HttpResponseRedirect,HttpResponse
from django.contrib import messages
from compass.forms import *
from compass.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth import authenticate, login

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form })
    return render_to_response('registration/register.html',variables )

def register_success(request):
    return render_to_response('registration/success.html')




def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def enquiry(request):
    context = RequestContext(request)	
    if request.method == "POST":
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry = enquiry_form.save()
	    
        else:
            print enquiry_form
    else:
        enquiry_form = EnquiryForm()
    return render_to_response('index.html',
     {'enquiry_form': enquiry_form}, context)

def message(request):
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            message = message_form.save()
            done = True
        else:
            print message_form
    else:
        print "hi"
    return render_to_response(request, 'index.html',
     {'message_form': message_form,
     'done': done}, context)

def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'registration/login.html', {})

