from django.shortcuts import render
from .forms import ProductUploadForm

def upload_product(request):
    
  if request.method == "POST":
    form = ProductUploadForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
  else:
      form = ProductUploadForm()   
         
  return render(request, 'inventory/product_upload.html', {'form': form})
 

# it is sent in a dictionary format thus the {}



# Create your views here.
