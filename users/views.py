from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required # این خط را به بالای فایل اضافه کنید
from orders.models import Order # این خط را به بالای فایل اضافه کنید

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login') # بعد از ثبت‌نام به صفحه ورود می‌رود
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# ... (تابع register در جای خود باقی می‌ماند)

@login_required(login_url='users:login')
def profile(request):
    # دریافت سفارشات متعلق به کاربر فعلی
    orders = Order.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'orders': orders})