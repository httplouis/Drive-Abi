from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    # ========================================================================
    # PUBLIC ROUTES
    # ========================================================================
    
    # Home & Basic Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    
    # Services
    path('rentcar/', views.rentcar, name='rentcar'), 
    path('buycar/', views.buycar, name='buycar'),
    
    # Public Car Views
    path('cars/', views.cartest, name='cartest'), 
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    
    # Other Pages
    path('news/', views.news, name='news'), 
    path('user/', views.user_profile, name='user'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'), 
    path('return/', views.return_instructions, name='return'),
    path('blog/', views.blog, name='blog'),
    path('customer/', views.customer_support, name='customer'),
    path('reviews/', views.reviews, name='reviews'),
    path('delivery/', views.delivery, name='delivery'),
    path('reservation/', views.reservation, name='reservation'),
    path('terms/', views.terms, name='terms'),
    path('car_description/', views.car_description, name='car_description'),
    path('promotional/', views.promotional, name='promotional'),
    
    # Forms
    path('m/', views.homepage, name='m'),
    path('membership/', views.mem, name='membership'),
    path('sign/', views.s, name='sign'),
    
    # ========================================================================
    # ADMIN ROUTES
    # ========================================================================
    
    # Admin Dashboard
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    
    # Admin Car Management
    path('admin/cars/', views.admin_car_manage, name='admin_car_manage'),
    path('admin/cars/create/', views.admin_car_create, name='admin_car_create'),
    path('admin/cars/<int:pk>/update/', views.admin_car_update, name='admin_car_update'),
    path('admin/cars/<int:pk>/delete/', views.admin_car_delete, name='admin_car_delete'),
]
