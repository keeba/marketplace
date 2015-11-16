from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from catalog.models import Category,SubCategory,Product,Catalog
from catalog.serializers import CategorySerializer,SubCategorySerializer,ProductSerializer,CatalogSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
    def perform_create(self,serializer):
        serializer.save(seller=self.request.user)
    
    def get_queryset(self):    
        request = self.request
        if request.user.is_authenticated():
            return Catalog.objects.filter(seller=request.user)
        else: 
            return Catalog.objects.all()