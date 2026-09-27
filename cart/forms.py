from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1, 
        max_value=10, 
        initial=1, 
        label="تعداد",
        widget=forms.NumberInput(attrs={'class': 'w-20 text-center border border-gray-300 rounded-lg py-2 px-2 ml-4 focus:outline-none focus:border-yellow-500'})
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)