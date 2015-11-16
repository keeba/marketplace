from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Category,SubCategory,Product,Catalog
from django.db.models import F

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
        
class SubCategorySerializer(serializers.ModelSerializer):
    category_data = CategorySerializer(source="category",read_only=True)    
    class Meta:
        model = SubCategory
        fields = ('id','name','category','category_data')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()  
    price = serializers.SerializerMethodField()  
    is_available = serializers.SerializerMethodField() 
    user = serializers.IntegerField(source="user.id",read_only=True) 
    category_id = serializers.SerializerMethodField()          
    sellers = serializers.SerializerMethodField()    
    class Meta:
        model = Product
        fields = ('id','title','description','subcategory','category','price','is_available','user','can_delete',
                 'category_id','sellers')
        
    def get_category(self,obj):
        return obj.subcategory.__str__()  
    
    def get_price(self,obj):
        return obj.get_min_price()
        
    def get_is_available(self,obj):            
        return obj.is_available()  
    
    def get_can_delete(self,obj):
        return obj.can_delete()  
        
    def get_category_id(self,obj):
        return obj.subcategory.category_id
    
    def get_sellers(self,obj):
        sellers = obj.catalog_set.all().order_by('price').values('seller__first_name','price','available_count')    
        for seller in sellers:
            seller['name'] = seller['seller__first_name']
            seller.pop('seller__first_name',None)
        return sellers    
            
class CatalogSerializer(serializers.ModelSerializer):
    seller = serializers.IntegerField(source="user.id",read_only=True)
    product_title = serializers.SerializerMethodField()
    product_category = serializers.SerializerMethodField()  
    class Meta:
        model = Catalog
        fields = ('id','product','price','available_count','seller','product_title','product_category')        
    
    def get_product_title(self,obj):
        return obj.product.title
        
    def get_product_category(self,obj):
        return obj.product.subcategory.__str__()
        
        
