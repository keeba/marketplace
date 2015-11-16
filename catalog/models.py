from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category) 
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.category.name + ' - ' + self.name
    
class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    subcategory = models.ForeignKey(SubCategory) 
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['id']
        
    def get_min_price(self):
        catalog = self.catalog_set.all().order_by('price')[:1]
        if catalog:
            return 'Rs. '+ str('{:g}'.format(catalog[0].price))
        else:
            return None    
    def is_available(self):
        count = self.catalog_set.filter(available_count__gt=0).count()      
        if count:
            return 'Yes'
        else:
            return 'No' 
            
    def can_delete(self):           
        sellers_count = self.catalog_set.all().count()
        if sellers_count < 1:
            return 1
        elif sellers_count == 1:
            seller = self.catalog_set.all()[:1]
            if seller[0].seller_id == self.user_id:
                return 1
        return 0
        
class Catalog(models.Model):
    product = models.ForeignKey(Product) 
    price = models.FloatField()
    available_count = models.IntegerField()
    seller = models.ForeignKey(User,related_name="seller") 