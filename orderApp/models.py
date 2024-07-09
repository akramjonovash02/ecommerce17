from django.db import models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    delivery_date = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    total_payment = models.DecimalField()
    payment_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} ({self.user.username})"
