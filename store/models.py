from django.db import models

# table for products:
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
# ----------------------------------------------------------------------------
# table for orders:

class Order(models.Model):
    status = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=status, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id}'
# ------------------------------------------------------------------------------
# table for order items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_cost(self):
        return self.price * self.quantity
