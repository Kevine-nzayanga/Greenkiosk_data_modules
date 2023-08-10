from django.shortcuts import render
from .forms import CustomerUploadForm
from .models import Customer
from django.shortcuts import redirect

def customer_signup(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save()
            customer.save()
    else:
        form = CustomerUploadForm()

    return render(request, 'customer/customer_signup.html', {"form": form})

 
  
def customer_list(request):
    customers = Customer.objects.all()
    return render(request,'customer/customer_list.html',{"customers":customers} )


def edit_customer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, instance=customer)
        if form.is_valid():
          form.save()
          
          return redirect("customer_detail_view",id = customer.id)
      
    else:
          form = CustomerUploadForm(instance=customer)
          return render(request,"customer/edit_customer.html", {"form":form})
 
 
def customer_details(request,id):
    customer=Customer.objects.get(id= id)
    
    return render(request, "customer/customer_detail.html",{"customer":customer})
     

          
    
     
            
            
            


# Create your views here.
