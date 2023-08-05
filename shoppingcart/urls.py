from django.urls import path
from.views import cart_products

urlpatterns = [
    path("cart/list/", cart_products, name="cart_product_view")
]


