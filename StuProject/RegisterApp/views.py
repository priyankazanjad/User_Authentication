from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    template_name = 'RegisterApp/register.html'
    return render(request,template_name,context)

def loginView(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pw')
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('show_stu')
        else:
            messages.error(request,'Invalid Credentials')
    context = {}
    template_name = 'RegisterApp/login.html'
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

