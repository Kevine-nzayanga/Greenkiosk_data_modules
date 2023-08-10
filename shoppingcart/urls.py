from django.urls import path
from.views import cart_products,edit_cart

urlpatterns = [
    path("cart/list/", cart_products, name="cart_product_view"),
    path("cart/edit/<int:id>/",edit_cart, name="edit_cart_view" )
]


