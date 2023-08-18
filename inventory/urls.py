from django.urls import path
from django.conf import settings
from django.conf.urls.static  import static
from .views import upload_product, product_list, product_detail,edit_product


urlpatterns= [
    path("products/upload/", upload_product,name="product_upload_view"),
    path("products/list/",product_list, name="products_list_view"),
    path("products/<int:id>/",product_detail, name= "products_detail_view"),
    path("products/edit/<int:id>/", edit_product, name="edit_product_view")
    ]

