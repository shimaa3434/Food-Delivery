from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import Category, Order, MenuItem
from django.db.models import Q
import json


class Index(View):
    def get(self, request, *args, **kwargs):
        categories= Category.objects.filter(parent= None)
        context= {'categories': categories}
        return render(request, 'customer/index.html', context)

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html', {})


class Order_view(View):
    def get(self,request, *args, **kwargs):
        cat= Category.objects.all()
        context= {'cat': cat}
        return render(request, 'customer/order.html', context)
    def post(self, request, *args, **kwargs):
        name= request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip-code')
        order_items= {'items': []}
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item= MenuItem.objects.get(pk__contains= int(item))
            item_data= {'id': menu_item.pk, 'name': menu_item.name, 'price': menu_item.price}
            order_items['items'].append(item_data)
            price= 0
            item_ids= []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        order= Order.objects.create(price= price, name=name, email= email, street= street, city= city, state= state, zip_code= zip_code)
        order.items.add(*item_ids)
        #بعد تنفيذ واضافة العناصر إلى كلاس الطلبات سوف يتم ارسال اسميل إلى طالب الاكل
        subject= 'شكرا للتعاملك معنا'
        body= 'السلام عليكم ورحمة الله وبركاته \n' \
              f'يسعدنا تقديم طلباكم في أسرع وقت ممكن واجمالي المدفوعات هو {price}\n' \
              'وشكرا لكم وأتمني لكم أسعد الأوقات'
        send_mail(subject, body, 'bwmn900@gmail.com', [email], fail_silently= False)
        context= {'items': order_items['items'], 'price': price}
        return redirect('order-confirmation', pk= order.pk)

class Order_confirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order= Order.objects.get(pk= pk)
        context= {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/order_comfirmtion.html', context)

    def post(self, request, pk, *args, **kwargs):
        data= json.loads(request.body)
        order = Order.objects.get(pk=pk)
        if data['is_paid']:
            order.is_paid = True
            order.save()
        return redirect('order_pay_confirmation')

class Order_pay_confirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_comfirmtion.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items= MenuItem.objects.all()
        context = {'menu_items': menu_items}
        return render (request, 'customer/menu.html', context)

class Menu_Search(View):
    def get(self, request, *args, **kwargs):
        q= self.request.GET.get('q')
        menu_items = MenuItem.objects.filter(Q(name__icontains = q) | Q(price__icontains = q) | Q(category__name__icontains = q) | Q(des__icontains = q))
        context = {'menu_items': menu_items}
        return render(request, 'customer/menu.html', context)