from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# تابع قبلی (صفحه اصلی)
def home_page(request):
    # دریافت ۴ دسته‌بندی اول
    categories = Category.objects.all()[:4]
    # دریافت ۴ ساعت جدید برای بخش برگزیده هفته
    latest_products = Product.objects.filter(available=True)[:4]
    
    return render(request, 'shop/index.html', {
        'products': latest_products,
        'categories': categories
    })
    

# تابع جدید (صفحه فروشگاه و فیلتر دسته‌بندی‌ها)
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    # اگر کاربر روی یک دسته‌بندی خاص کلیک کرده بود
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    # تنظیم حداکثر تعداد مجاز برای انتخاب، بر اساس موجودی انبار همان ساعت
    cart_product_form.fields['quantity'].max_value = product.stock
    cart_product_form.fields['quantity'].widget.attrs['max'] = product.stock
    
    return render(request, 'shop/product_detail.html', {
        'product': product, 
        'cart_product_form': cart_product_form 
    })