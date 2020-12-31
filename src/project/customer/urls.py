"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import Index, About, Order_view, Order_confirmation, Order_pay_confirmation, Menu, Menu_Search

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('order/', Order_view.as_view(), name='order'),
    path('confirmation/<int:pk>', Order_confirmation.as_view(), name='order-confirmation'),
    path('order_pay_confirmation/', Order_pay_confirmation.as_view(), name='order_pay_confirmation'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', Menu_Search.as_view(), name='menu_search'),
]
