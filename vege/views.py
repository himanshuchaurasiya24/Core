from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
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
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
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
def login_page(request):
    return render(request, 'login.html')
def register_page(request):
    return render(request, 'register.html')