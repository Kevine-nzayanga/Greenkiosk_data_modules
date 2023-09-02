from rest_framework.views import APIView
from customer.models import Customer
from .serializers import CustomerSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Product

class CustomerListView(APIView):
    def get(self, request):
        customers= Customer.objects.all()
        serializer= CustomerSerializer(customers, many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomerDetailView(APIView):
    def get (self, request, id, format=None ):
        customer = Customer.objects.get(id=id)
        serializer= CustomerSerializer(customer)
        return Response (serializer.data)
    
    def put(self,request,id,format= None):
        customer = Customer.objects.get(id=id)
        serializer= CustomerSerializer(customer, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format= None):
        customer= Customer.objects.get(id=id)
        customer.delete()
        return Response("custoner deleted", status=status.HTTP_204_NO_CONTENT)
    

class ProductListView(APIView):
    def get(self, request):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product)
        return Response (serializer.data)
    
    def put(self,request,id,format=True):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format= None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response("Product deleted", status= status.HTTP_204_NO_CONTENT)
        
    
        
        
    
    
        
        


# Create your views here.
