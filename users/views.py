from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def profile(request):
    
    return render(request, 'users/profile.html')

def register(request):
      #put a check in place
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            
            return redirect('login')
    else:
        form = UserCreationForm(request.POST)
    return render(request,'users/register.html',{'form':form})  