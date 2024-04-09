from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        quantity = request.POST['quantity']
        new_sales = AddStock(first_name=first_name,last_name=last_name,quantity=quantity)
        new_sales.save()
        print(first_name,last_name,quantity)
        message = 'Record Taken Successfuly'
        return(HttpResponse(message))
