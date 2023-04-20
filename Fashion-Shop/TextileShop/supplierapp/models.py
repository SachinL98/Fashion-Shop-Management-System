from django.db import models

# Create your models here.
CATEGORY = (
    ('Trousers','Trousers'),
    ('Saree','Saree'),
    ('Lungi','Lungi'),
    ('Frocks','Frocks'),
    ('Jeans','Jeans'),
    ('Shirts','Shirts'),
)

class Supplier(models.Model):
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=20,choices=CATEGORY,null=True)

class Meta:
    verbose_name_pural ="supdatabase"     
