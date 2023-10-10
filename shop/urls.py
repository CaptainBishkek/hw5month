"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.category_list, name='category-list'),
    path('api/v1/categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('api/v1/products/', views.product_list, name='product-list'),
    path('api/v1/products/<int:pk>/', views.product_detail, name='product-detail'),
    path('api/v1/reviews/', views.review_list, name='review-list'),
    path('api/v1/reviews/<int:pk>/', views.review_detail, name='review-detail'),
    path('products/reviews/', views.product_reviews, name='product-reviews'),
]
