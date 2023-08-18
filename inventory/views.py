from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product
from django.shortcuts import redirect

def upload_product(request):
  
  if request.method == "POST":
    # upload_product = request.FILES.get("images", None)
    # upload_product = request.FILES["images"]
    form = ProductUploadForm(request.POST,request.FILES)
    if form.is_valid():
      product = form.save(commit=False)
      product.image = upload_product
      product.save()
  else:
      form = ProductUploadForm()   
  

  return render(request, 'inventory/product_upload.html',{ "form": form} )

 

# it is sent in a dictionary format thus the {}

def product_list(request):
  
  products= Product.objects.all()
  return render(request,"inventory/product_list.html", {"products":products})

# Create your views here.    </body>

def product_detail(request,id):
  product = Product.objects.get(id = id)
  return render(request,"inventory/product_detail.html", {"product":product})


def edit_product(request, id):
  product= Product.objects.get(id = id)
  if request.method == "POST":
    form= ProductUploadForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      
      return redirect("products_detail_view", id= product.id)
  else:
    form= ProductUploadForm(instance = product)
    return render (request, "inventory/edit_product.html", {"form":form})   
  
   

