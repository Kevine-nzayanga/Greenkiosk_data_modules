from django.shortcuts import render
from .forms import CustomerUploadForm
from .models import Customer
from django.shortcuts import redirect

def signup_customer(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            customer=form.save()
            customer.save()
    else:
     form=CustomerUploadForm()   
     
     return render (request, 'customer/customer_signup.html', {"form":form})
 
def customer_details(request):
    customer=Customer.objects.get(id= id)
    
    return render(request, "customr/customer_details.html",)
     
 
def edit_customer(request):
    customer = Customer.objects(id=id)
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, instance=customer)
        if form.is_valid():
          form.save()
          
          return redirect("customer_view",id = customer.id)
      
    else:
          form = CustomerUploadForm(instance=customer)
          return render(request,"customer/edit_customer.html", {"form":form})
          
    
     
            
            
            


# Create your views here.
