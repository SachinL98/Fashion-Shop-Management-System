from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from supplierapp.models import Supplier
#from supplierapp.models import  Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','address','type']
