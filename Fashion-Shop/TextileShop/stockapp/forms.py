from django import forms
from stockapp.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_code', 'brand','colour', 'size', 'category', 'quantity', 'price']