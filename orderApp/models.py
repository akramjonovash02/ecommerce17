from django.core.validators import MinValueValidator
from django.db import models

from mainApp.models import *
from userApp.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.amount}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('1', 'confirmate is pending'),
        ('2', 'is being collected'),
        ('3', 'is being delivered'),
        ('4', 'successfully'),
        ('5', 'canceled'),
    )
    PAYMENT_CHOICES = (
        ('CASH', 'CASH'),
        ('CARD', 'CARD')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    delivery_date = models.DateField()
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=500)
    total_payment = models.FloatField(validators=[MinValueValidator(0)])
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} ({self.user.username})"
