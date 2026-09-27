from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('products/', views.product_list, name='product_list'), # لیست کل ساعت‌ها
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'), # لیست فیلتر شده بر اساس دسته
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'), # مسیر جزئیات محصول بر اساس آیدی و اسلاگ
]