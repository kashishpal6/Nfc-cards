from django.db import models
from auth_app.models import CustomUser
from variant.models import variant

class Payment(models.Model):
    payment_id = models.CharField(max_length=100,default='default')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="payment")   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')
    ], default='pending')
    payment_method = models.CharField(max_length=50, default='NFC')
    payment_at = models.DateTimeField(auto_now_add=True)
    product_variation = models.ForeignKey(variant,on_delete=models.CASCADE,related_name="variation")
    UTR = models.CharField(max_length=100,default='blank')

    def __str__(self):
        return self.user.email 

    class Meta:
        ordering = ['status']  

