from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def receipes(request):
    if request.method=='POST':
        data = request.POST
        receipe_image1 = request.FILES.get('receipe_image')
        receipe_name1= data.get('receipe_name')
        receipe_description1=data.get('receipe_description')
        print(receipe_name1)
        print(receipe_description1)
        print(receipe_image1)
        Receipe.objects.create(receipe_name=receipe_name1, receipe_description=receipe_description1, receipe_image= receipe_image1)
        receipe= Receipe.objects.all()
        print(receipe)
        for rec in receipe:
            print(rec.receipe_name)
            print(rec.receipe_description)
            print(rec.receipe_image)
        return redirect('/receipes/')
    return render(request, 'receipes.html')