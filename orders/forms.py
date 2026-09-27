from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'city', 'postal_code', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-3'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-3'}),
            'phone': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-3'}),
            'city': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-3'}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full border rounded-lg p-3'}),
            'address': forms.Textarea(attrs={'class': 'w-full border rounded-lg p-3', 'rows': 3}),
        }