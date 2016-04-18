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
from django.db.models import Q

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
    enquiry_form = EnquiryForm(data=request.POST)
    message_form = MessageForm(data=request.POST)
    if request.method == "POST":
        if "singlebutton" in request.POST and enquiry_form.is_valid():
            enquiry = enquiry_form.save()
	    
        if "message" in request.POST and message_form.is_valid():
            message = message_form.save()
    else:
        enquiry_form = EnquiryForm()
    return render_to_response('index.html',
     {'enquiry_form': enquiry_form, 'message_form':message_form}, context)


def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'registration/login.html', {})

def search(request):
    context = RequestContext(request)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    print q
    
    track = Track.objects.filter(Q(reference_no__iexact = q) | Q(status__iexact=q))
    for i in track:
        print "hii"
    return render_to_response('search.html', {'track': track}, context)


def status(request, reference_no):   
    t = Track.objects.get(reference_no=reference_no)
    status = CurrentStatus.objects.filter(reference_no=t)    
    template_name = 'status.html'
    context_dict = {'status': status, 't':t}
    return render(request, template_name, context_dict)

