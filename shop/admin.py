from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # این خط باعث می‌شود با تایپ نام، فیلد slug خودکار پر شود

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available'] # امکان ویرایش سریع این فیلدها از همان صفحه لیست
    prepopulated_fields = {'slug': ('name',)}