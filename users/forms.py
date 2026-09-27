from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اضافه کردن کلاس‌های استایل به تمام فیلدهای فرم
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full border rounded-lg p-3 mt-1 mb-4 focus:outline-none focus:border-yellow-500'