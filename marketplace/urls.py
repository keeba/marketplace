from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketplace import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login_user,name='login'),
    url(r'^logout/$',views.logout_user,name='logout'),
    url(r'^api/', include('catalog.urls')),  
)
