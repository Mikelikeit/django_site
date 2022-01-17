from django.shortcuts import render
from .models import Order


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    name_phone = Order.objects.create(order_name=name, order_phone=phone)
    return render(request, './thanks.html', {'name': name})
