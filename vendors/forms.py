from django import forms
from .models import Vendor

class VendorSignUpForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields="__all__"