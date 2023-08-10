from django.shortcuts import render
from .models import Order
from .forms import OrderUploadForm
from django.shortcuts import redirect


def orders_list(request):
    orders= Order.objects.all()
    return render(request, "order/order_list.html", {"orders":orders})


def order_upload(request):
    if request.method=="POST":
        form = OrderUploadForm(request.POST)
        
        if form.is_valid():
            order= form.save()
            order.save()
    else:
        form = OrderUploadForm()
    return render(request,"order/order_upload.html",{"form":form})           
 
 
def order_details(request,id):    
    order= Order.objects.get(id=id)
    return render (request,"order/order_details.html",{"order":order})


def edit_order(request,id):
    order= Order.objects.get(id = id)
    
    if request.method =="POST":
        form= OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
        return redirect("order_details_view", id=order.id)
    
    else:
        form = OrderUploadForm(instance=order)    
        return render(request, "order/edit_order.html",{"form":form})
         
        
    
    
    
    
    
    
    
    
    
# Create your views here.
