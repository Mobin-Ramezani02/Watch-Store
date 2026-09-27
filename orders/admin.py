from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0 # برای جلوگیری از نمایش سطرهای خالی اضافی

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'phone', 'city', 'paid', 'created']
    list_filter = ['paid', 'created', 'city']
    search_fields = ['first_name', 'last_name', 'phone', 'address']
    inlines = [OrderItemInline] # این خط باعث می‌شود آیتم‌های هر سفارش درون همان صفحه سفارش نمایش داده شوند