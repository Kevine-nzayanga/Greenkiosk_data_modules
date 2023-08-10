from django.urls import path
from .views import order_details,order_upload,orders_list,edit_order

urlpatterns = [
    path('order/upload/',order_upload, name= "order_upload_view"),
    path('order/details/<int:id>/',order_details, name="order_details_view"),
    path('order/list/', orders_list, name="orders_list_view"),
    path('order/edit/<int:id>/',edit_order, name="edit_order_view" )
]
