from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Coke Oven','Coke Oven'),
    ('Blast Furnace','Blast Furnace'),
)
class Product(models.Model):
    #   product_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

class Meta:
    verbose_name_plural = 'Staff Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Transactions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    transaction_quantity = models.PositiveIntegerField(null=True)
    date  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Transaction'
        



    def __str__(self):
        return f'{self.product.name} ordered by {self.staff.username}' 

