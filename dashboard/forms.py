from django import forms
from .models import Product, Transactions

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['product', 'transaction_quantity']
