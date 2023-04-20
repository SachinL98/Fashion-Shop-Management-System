from django.db import models
from dashboard.widget import DatePickerInput

# Create your models here.
SIZE = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L')
)

class Sales(models.Model):
    Date = models.DateField(max_length=10, null=True)
    Item_code = models.CharField(max_length=100)
    Item_name = models.CharField(max_length=100, null=True)
    Size = models.CharField(max_length=100, choices=SIZE, null=True)
    Price = models.FloatField(null=True)
    total_price=models.FloatField(null=True)
    QTY = models.PositiveIntegerField(null=True) 

    @property
    def totalPrice(self):
        self.total_price=self.Price*self.QTY
        return self.total_price

class Meta:
    db_table="Sales"