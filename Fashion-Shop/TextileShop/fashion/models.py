from django.db import models
from django.contrib.auth.models import User



departments=[('Kids','Kids'),
('Teens','Teens'),
('Gents','Gents'),
('Ladies','Ladies'),
('Officewear','Officewear'),
('Baby','Baby')
]

CATEGORY = (
    ('Womens', 'Womens' ),
    ('Mens', 'Mens' ),
    ('Kids', 'Kids' ),
)

SIZE = (
    ('XS', 'XS' ),
    ('S', 'S' ),
    ('M', 'M' ),
    ('L', 'L' ),
    ('XL', 'XL' ),
    ('XXL', 'XXL' ),
    ('XXXL', 'XXXL' ),
)

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    item_code = models.IntegerField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, choices=SIZE, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)



    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Ordermngr(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/OrdermngrProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.PositiveIntegerField(max_length=10,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Kids')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Supplier(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/SupplierProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.PositiveIntegerField(max_length=10,null=False)
    email = models.EmailField(max_length=100,null=False)
    item_code = models.CharField(max_length=100,null=False)
    assignedOrdermngrId = models.PositiveIntegerField(null=False)
    confirmedDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.item_code+")"


class Order(models.Model):
    supplierId=models.PositiveIntegerField(null=False)
    ordermngrId=models.PositiveIntegerField(null=False)
    supplierName=models.CharField(max_length=40,null=True)
    ordermngrName=models.CharField(max_length=40,null=True)
    orderDate=models.DateField(auto_now=True)
    item_code=models.CharField(max_length=10)
    brand = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, choices=SIZE, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity=models.PositiveIntegerField(null=False)
    status=models.BooleanField(default=False)



class SupplierCancelDetails(models.Model):
    supplierId=models.PositiveIntegerField(null=False)
    supplierName=models.CharField(max_length=40)
    assignedOrdermngrName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.PositiveIntegerField(max_length=10,null=True)
    item_code = models.CharField(max_length=10,null=True)
    brand = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, choices=SIZE, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)

    confirmedDate=models.DateField(null=False)
    cancelledDate=models.DateField(null=False)

    units=models.PositiveIntegerField(null=False)
    quantity=models.PositiveIntegerField(null=False)
    Othercharges=models.PositiveIntegerField(null=False)
    Transportfee=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)

