from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس اینترنتی (Slug)")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', verbose_name="دسته‌بندی‌ها")
    name = models.CharField(max_length=200, verbose_name="نام ساعت")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس اینترنتی (Slug)")
    brand = models.CharField(max_length=100, verbose_name="برند")
    description = models.TextField(verbose_name="توضیحات ساعت")
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="قیمت (تومان)")
    image = models.ImageField(upload_to='products/%Y/%m/', verbose_name="تصویر ساعت")
    stock = models.PositiveIntegerField(verbose_name="موجودی در انبار")
    available = models.BooleanField(default=True, verbose_name="نمایش در سایت")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    class Meta:
        ordering = ('-created',)
        verbose_name = "ساعت"
        verbose_name_plural = "ساعت‌ها"

    def __str__(self):
        return self.name