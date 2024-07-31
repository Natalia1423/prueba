from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def home (request):
    return render(request,'home.html')

def index (request):

    if request.method == 'GET':
          return render (request,'index.html',{
            'form': UserCreationForm
    }) 
    else:
         if request.POST ['password1'] == request.POST ['password2']:
            try:
               User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
               User.save ()
               #return HttpResponse ('usuario creado')
               return redirect('index')
            except:
                            return HttpResponse ('Usuario ya existe')
    return HttpResponse ('Contraseña no coincide')
    

