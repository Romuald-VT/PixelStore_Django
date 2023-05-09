from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Account
from .forms import RegistrationForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

import pdb

# Create your views here.

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
             First_Name = form.cleaned_data['first_name']
             Last_Name = form.cleaned_data['last_name']
             Email = form.cleaned_data['email']
             Phone_Number = form.cleaned_data['phone_number']
             Passsword = form.cleaned_data['password']
             Username = Email.split('@')[0]
             
             user = Account.objects.create_user(First_Name, Last_Name, Username, Email,Phone_Number,password=Passsword)
             user.save()
             messages.success(request, 'Inscription reussie !')
    else:
            form = RegistrationForm()
              
    context={'form': form,}
    
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'vous etes connectes')
            return redirect('home')
        else:
            messages.error(request, 'email et/ou mot de passe incorrects !')
            return redirect('login')
    return render(request,'accounts/login.html',)

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Vous etes deconnecte !')
    return redirect('login')

def forgot_password(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
         
        if Account.objects.filter(email=email).exists():
           user =Account.objects.get(email__exact = email)
           if password == confirm_password:
               user.password = password
               user.save()
               messages.success(request,'mot de passe mis a jour !')
           else:
               messages.error(request, 'les mots de passes ne correspondent pas !')
        else:
            messages.error(request, "cet email n'existe pas ! ")
    return render(request,'accounts/forgot_password.html')


