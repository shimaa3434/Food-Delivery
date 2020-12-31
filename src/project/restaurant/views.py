from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from customer.models import Order
from django.utils.timezone import datetime
# Create your views here.

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        today= datetime.today()
        orders= Order.objects.filter(created_on__year= today.year, created_on__month= today.month, created_on__day= today.day)
        total_orders= len(orders)
        total=0
        shipped = 0
        not_shipped = 0
        for order in orders:
            total += order.price
            if order.is_shipped:
                shipped += order.is_shipped
            else:
                not_shipped += 1
        context= {
            'total':total,
            'total_orders': total_orders,
            'orders': orders,
            'shipped': shipped,
            'not_shipped': not_shipped,
        }
        return render (request, 'restaurant/dashbord.html', context)




class Order_Details(View):
    def get(self, request, pk, *args, **kwargs):
        order= Order.objects.get(pk= pk)
        context= {
            "order": order
        }
        return render(request, 'restaurant/order_details.html', context)


    def post(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        order.is_shipped = True
        order.save()
        context = {
            "order": order
        }
        return render(request, 'restaurant/order_details.html', context)