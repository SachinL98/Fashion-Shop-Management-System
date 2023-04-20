from django.db import models
from stockapp.models import Item

# Create your models here.

CATEGORY=(
    ('Electricity','Electricity'),
    ('Water','Water'),
)

class utilitybill(models.Model):
    bill_id=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    date =models.DateField(max_length=100, null=True)
    price=models.FloatField(null=True)
class Meta:
    db_table="utilitybill"

class employee_salasry(models.Model):
    empid=models.CharField(max_length=20,null=True)
    basic_Salary=models.FloatField(null=True)
    OT_houres=models.PositiveIntegerField(null=True)
    OT_Rate=models.FloatField(null=True)
    deduction=models.FloatField(null=True)
    increment=models.FloatField(null=True)
    total_sal=models.FloatField(null=True)
    date =models.DateField(max_length=100, null=True)

    @property
    def netsal(self):
        self.total_sal=((self.basic_Salary*self.OT_Rate)/100.00)*float(self.OT_houres)+self.basic_Salary+(self.increment-self.deduction)
        return self.total_sal
    

class Meta:
    db_table="employee_salasry"




class Order(models.Model):
    supplierId=models.PositiveIntegerField(null=True)
    ordermngrId=models.PositiveIntegerField(null=True)
    item_code=models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(null=True)
    orderDate=models.DateField(max_length=100,null=True)
    status=models.BooleanField(null=True)
    total_price=models.FloatField(null=True)
    ordermngrName=models.CharField(max_length=50,null=True)
    supplieName=models.CharField(max_length=50,null=True)

    @property
    def totalPrice(self):
        self.total_price=self.item_Id.price*self.quantity_order
        return self.total_price

class Meta:
    db_table="fashion_order"

