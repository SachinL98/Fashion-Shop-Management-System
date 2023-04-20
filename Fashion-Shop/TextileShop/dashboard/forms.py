from django import forms
from dashboard.models import employee_salasry
from dashboard.models import utilitybill
from dashboard.widget import DatePickerInput

class ExampleForm(forms.Form):
       date = forms.DateField(widget=DatePickerInput)

class employeesalForm(forms.ModelForm):
    class Meta:
        model=employee_salasry
        fields=[
            'empid',
            'basic_Salary',
            'OT_houres',
            'OT_Rate',
            'deduction',
            'increment',
            'date'
        ]
        widgets = {
            'date' : DatePickerInput(),
        }


class ExampleForm(forms.Form):
       date = forms.DateField(widget=DatePickerInput)

class utilitybillForm(forms.ModelForm):
    class Meta:
        model=utilitybill
        fields=[
            'bill_id',
            'category',
            'date',
            'price'
        ]
        widgets = {
            'date' : DatePickerInput(),
        }