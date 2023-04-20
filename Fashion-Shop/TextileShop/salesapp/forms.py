from django import forms
from salesapp.models import Sales

class DatePickerInput(forms.DateInput):
    input_type='date'

class ExampleForm(forms.Form):
    Date = forms.DateField(widget=DatePickerInput)

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = [
        'Date',
        'Item_code',
        'Item_name',
        'Size',
        'Price',
        'QTY'
        ]
        widget = {
            'Date' : DatePickerInput(),
        }

