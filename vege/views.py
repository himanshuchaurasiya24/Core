from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
from django.db.models import Q, Sum
def get_student(request):
    queryset= Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset= queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_age__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_address__icontains=search)
        )
    paginator = Paginator(queryset, 25)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request,'report/students.html' ,{'queryset':page_obj})
def see_marks(request ,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    return render(request, 'report/see_result.html', {'queryset':queryset,'total_marks':total_marks})