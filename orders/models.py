from django.db import models
from django.contrib.auth.models import User # این خط اضافه شد
from shop.models import Product

class Order(models.Model):
    # این فیلد جدید اضافه شد (null و blank مساوی True است تا سفارشات مهمان به مشکل نخورد)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True, verbose_name="کاربر")
    
    first_name = models.CharField(max_length=50, verbose_name="نام")
    # ... (بقیه فیلدهای کلاس Order دقیقاً مثل قبل باقی بماند)
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    address = models.TextField(verbose_name="آدرس دقیق")
    postal_code = models.CharField(max_length=20, verbose_name="کد پستی")
    city = models.CharField(max_length=100, verbose_name="شهر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")

    class Meta:
        ordering = ('-created',)
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return f'سفارش {self.id}'

# کلاس OrderItem هم دقیقاً مثل قبل باقی می‌ماند
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)