from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            if request.user.is_authenticated:
                order.user = request.user
                
            order.save() 
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                
                # --- کدهای اضافه شده برای کسر موجودی انبار ---
                product = item['product']
                product.stock -= item['quantity']
                
                # اگر موجودی ساعت به صفر رسید، تیک "نمایش در سایت" را خودکار بردار
                if product.stock <= 0:
                    product.stock = 0
                    product.available = False
                    
                product.save()
                # ---------------------------------------------
                
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})