from django.conf.urls import patterns, url,include
from catalog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubCategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'catalog', views.CatalogViewSet)

urlpatterns = patterns('',
    url(r'', include(router.urls)),    
)
