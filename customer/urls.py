from django.urls import path
from .views import signup_customer

urlpatterns = [
    path('customer/signup/', signup_customer, name='signup_view')
    
]
