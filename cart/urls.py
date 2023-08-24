from django.urls import path
from.views import cart_products,add_cart

urlpatterns = [
    path("cart/list/", cart_products, name="cart_product_view"),
    # path("cart/edit/<int:id>/",edit_cart, name="edit_cart_view" ),
    path('cart/<int:product_id>', add_cart,name="add_to_cart")
]


