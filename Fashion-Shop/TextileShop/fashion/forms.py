from django import forms
from django.contrib.auth.models import User
from fashion import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class OrdermngrUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class OrdermngrForm(forms.ModelForm):
    class Meta:
        model=models.Ordermngr
        fields=['address','mobile','department','status','profile_pic']
        widgets = {
            'mobile':forms.NumberInput()
        }



#for teacher related form
class SupplierUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class SupplierForm(forms.ModelForm):
  
    assignedOrdermngrId=forms.ModelChoiceField(queryset=models.Ordermngr.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Supplier
        fields=['address','mobile','status','email','item_code','profile_pic']
        
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("Email must contain @")
        if not ".com" in email:
            raise forms.ValidationError("Email must contain .com ")
        return email



class OrderForm(forms.ModelForm):
    ordermngrId=forms.ModelChoiceField(queryset=models.Ordermngr.objects.all().filter(status=True),empty_label="Ordermngr Name and Department", to_field_name="user_id")
    supplierId=forms.ModelChoiceField(queryset=models.Supplier.objects.all().filter(status=True),empty_label="Supplier Name", to_field_name="user_id")
 
    
    
    class Meta:
        model=models.Order
        fields=['item_code','brand','size','colour','category','status','quantity']
        
   
        


class SupplierOrderForm(forms.ModelForm):
    ordermngrId=forms.ModelChoiceField(queryset=models.Ordermngr.objects.all().filter(status=True),empty_label="Ordermngr Name and Department", to_field_name="user_id")
    
    class Meta:
        model=models.Order
        fields=['item_code','status','quantity']


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

