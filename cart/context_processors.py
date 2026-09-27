from .cart import Cart

def cart_context(request):
    """این تابع سبد خرید را در تمام صفحات سایت در دسترس قرار می‌دهد"""
    return {'cart': Cart(request)}