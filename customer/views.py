from django.shortcuts import render
from .forms import CustomerUploadForm

def signup_customer(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            customer=form.save()
            customer.save()
    else:
     form=CustomerUploadForm()   
     
     return render (request, 'customer/customer_signup.html', {"form":form})
 
            
            
            


# Create your views here.
