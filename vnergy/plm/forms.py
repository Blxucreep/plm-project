from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address', 'products_sold']
        widgets = {
            'products_sold': forms.Textarea(attrs={'rows': 3}),
        }
