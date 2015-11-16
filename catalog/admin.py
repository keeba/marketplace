from django.contrib import admin

# Register your models here.

from django.contrib import admin
from catalog.models import Category,SubCategory

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
admin.site.register(SubCategory, SubCategoryAdmin)
