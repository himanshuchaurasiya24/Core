from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def receipes(request):
    if request.method=='POST':
        data = request.POST
        receipe_image1 = request.FILES.get('receipe_image')
        receipe_name1= data.get('receipe_name')
        receipe_description1=data.get('receipe_description')
        Receipe.objects.create(receipe_name=receipe_name1, receipe_description=receipe_description1, receipe_image= receipe_image1)
        receipe= Receipe.objects.all()
        return redirect('/receipes/')
    queryset= Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context = {'receipes':queryset}
    return render(request, 'receipes.html', context)
@login_required(login_url='/login/')
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
@login_required(login_url='/login/')
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method =='POST':
        data = request.POST 
        receipe_image1 = request.FILES.get('receipe_image')
        receipe_name1= data.get('receipe_name')
        receipe_description1=data.get('receipe_description')
        queryset.receipe_name= receipe_name1
        queryset.receipe_description= receipe_description1
        if receipe_image1:
            queryset.receipe_image=receipe_image1
        queryset.save()
        return redirect('/receipes/')
        
    context = {'receipe':queryset}
    return render (request, 'update-receipe.html', context)
@login_required(login_url='/login/')
def logout_page(request):
    logout(request=request,)
    return redirect('/login/')
def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid password.')
            return redirect('/login/')
        else:
            login(user=user, request=request)
            return redirect('/receipes/')
    
    messages.info(request, 'username does not exists.')
    # return redirect('/login/')

    return render(request, 'login.html')
def register_page(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username1 = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username1)
        if user.exists():
            messages.info(request, 'username already taken.')
            return redirect('/register/')
        else:
            user = User.objects.create(first_name= first_name, last_name= last_name, username=username1)
            user.set_password(password)
            user.save()
            messages.info(request, 'Account Created Successfully')
            return redirect('/login/')
    return render(request, 'register.html')