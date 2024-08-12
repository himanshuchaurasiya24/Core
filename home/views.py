from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client
def send_email(request):
    send_email_to_client()
    return redirect('/')
def home(request):
    # seed_db(100)
    people =[
        {
        'name':'Abhijeet','age':26        
    },
      {
        'name':'Himanshu','age':24        
    },
      {
        'name':'Shishir','age':28        
    },
     {
        'name':'Anuj','age':22        
    },
     {
        'name':'Ankit','age':30        
    },
    ]
    text = 'sample text'
    vegetables = ['Pumpkin' , 'Tomatoo']
    # return HttpResponse('Hey home page of core project.')
    return render(request,'index.html', context={'people':people,'text':text,'vegetables':vegetables,'page':'Django Tutorial Index Page'})
def about(request):
    context = {'page':'About Page of Django Server'}
    return render(request, 'about.html', context)
def contact(request):
    context = {'page':'Contact Page of Django Server'}
    return render(request, 'contact.html', context)

def success_page(request):
    context = {'page':'Success Page of Django Server'}

    return HttpResponse('Hey this is a success page of django project.',context)
