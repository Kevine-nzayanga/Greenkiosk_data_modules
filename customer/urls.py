from django.urls import path
from .views import signup_customer,edit_customer,customer_details

urlpatterns = [
    path('customer/signup/', signup_customer, name='signup_view'),
    path('customer/edit/', edit_customer, name='edit_customer_view'),
    path('customer/details/',customer_details, name='customer_details_view')
    
]
