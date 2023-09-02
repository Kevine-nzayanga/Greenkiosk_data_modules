from django.urls import path
from.views import cart_products,cart_view,add_to_cart,remove_from_cart

urlpatterns = [
    path('view/', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path("cart/list/", cart_products, name="cart_product_view"),
    # path("cart/edit/<int:id>/",edit_cart, name="edit_cart_view" ),
    # path('cart/<int:product_id>', add_cart,name="add_to_cart")
]


