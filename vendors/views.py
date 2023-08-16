from django.shortcuts import render
from .forms import VendorSignUpForm
from .models import Vendor
from django.shortcuts import redirect


def vendor_signup(request):
    if request.method =="POST":
        form=VendorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            vendor=form.save()
            vendor.save()
    else:
        form=VendorSignUpForm()
        return render (request,'vendor/vendor_signup.html', {'form':form})
    
    
def vendor_list(request):
    vendors= Vendor.objects.all()    
    context={'vendors' : vendors}
    return render(request,"vendor/vendor_list.html",context )
  
  
def vendor_edit(request,id):
    vendor= Vendor.objects.get(id=id)  
    if request.method=="POST":
        form= VendorSignUpForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            
            return redirect("vendor_detail.html", id= vendor.id)  
    else:
        form= VendorSignUpForm(instance=vendor)
    return render(request,"vendor/vendor_edit.html",{"form":form})            
# Create your views here.
