from django.urls import path
from .views import vendor_signup, vendor_list, vendor_edit

urlpatterns = [
    path("vendor/signup/",vendor_signup, name="vendor_signup_view"),
    path("vendor/list/", vendor_list, name="vendor_list_view" ),
    path("vendor/edit/<int:id>/", vendor_edit, name="vendor_edit_view")
]
