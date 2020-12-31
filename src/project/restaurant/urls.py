from django.urls import path
from .views import Order_Details, Dashboard

urlpatterns = [
    path("dashboard/", Dashboard.as_view(), name= 'dashboeard'),
    path('order_details/<int:pk>', Order_Details.as_view(), name='order_details'),
]
