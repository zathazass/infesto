from django.shortcuts import render,redirect
#for-sending-mail
from django.core.mail import EmailMessage
#authenticate
from django.contrib.auth import authenticate,get_user_model,login,logout
#form
from .forms import UserLoginForm,UserRegisterForm,UserForm,ProfileForm
from . models import Profile,Event
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
import datetime
from infesto.utils import render_to_pdf #created in step 4
from django import template
from django.template.loader import get_template



class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        profiles = Profile.objects.all()
        context = {
            'profiles':profiles,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "register_list_%s.pdf" %("")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

def home(request):
    return render(request,'home.html')

def home_view(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'new_home.html',context)

def events(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request,'events.html',context)

def register_list(request):
    profiles = Profile.objects.all()

    context = {'profiles':profiles}
    return render(request,'register_list.html',context)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')

    context = { 'form': form }
    return render(request,'login.html',context)

def register_view(request):
    #next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        #user.is_active = False #newline
        password = form.cleaned_data.get('password')
        #if email.send():
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        #current_site = get_current_site(request)#newline
        mail_subject = "Account Registered Successfully"

        message = "Your Infesto 2k19 account has been registered successfully now you can login and edit your events."
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject,message,to=[to_email])
        #email.send()
        login(request,user)


        return redirect('profile_edit')

    context = { 'form': form }
    return render(request,'register.html',context)

def about(request):
    return render(request,'about.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):

    return render(request,'profile.html')
#######################edit Profile#@@@@@3###################
@login_required
def profile_edit(request):
    if request.method =='POST':
        u_form = UserForm(request.POST,instance=request.user)
        p_form = ProfileForm(request.POST,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile_edit.html',context)
