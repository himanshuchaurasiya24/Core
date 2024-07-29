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
    context = {'receipes':queryset}
    return render(request, 'receipes.html', context)
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')