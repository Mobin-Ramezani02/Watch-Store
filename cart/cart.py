from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        """مقداردهی اولیه سبد خرید"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        # اگر سبد خریدی در سشن وجود نداشت، یک سبد خالی ایجاد می‌کنیم
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """اضافه کردن یک ساعت به سبد خرید یا بروزرسانی تعداد آن"""
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            
        self.save()

    def save(self):
        """ذخیره تغییرات در سشن"""
        self.session.modified = True

    def remove(self, product):
        """حذف یک ساعت از سبد خرید"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """پیمایش ساعت‌های داخل سبد و دریافت اطلاعات آن‌ها از دیتابیس"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """محاسبه تعداد کل آیتم‌های داخل سبد خرید"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """محاسبه قیمت کل سبد خرید"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """خالی کردن کامل سبد خرید پس از ثبت سفارش"""
        del self.session[settings.CART_SESSION_ID]
        self.save()