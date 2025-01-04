from django.shortcuts import render
from .models import Order
# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {"object_list" : object_list})

def thanks_page(request):
    name = request.POST['name']
    element = Order(order_name=name)
    element.save()
    object_list = Order.objects.all()
    return render(request, './index.html', {"object_list" : object_list})