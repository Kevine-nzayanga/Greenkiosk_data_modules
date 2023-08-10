from django.urls import path
from .views import customer_signup,customer_details,edit_customer,customer_list

urlpatterns = [
    path('customer/signup/', customer_signup, name='customer_signup_view'),
    path('customer/list/', customer_list, name = 'customer_list_view'),
    path('customer/edit/<int:id>/', edit_customer, name='edit_customer_view'),
    path('customer/details/<int:id>/',customer_details, name='customer_detail_view')
    
]
