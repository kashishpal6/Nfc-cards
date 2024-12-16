from django.db import models
from purchase.models import Purchase

class ReturnPage(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="pages")  
    image = models.ImageField(upload_to='returns/')
    reason = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('rejected', 'Rejected'),
        ], 
        default='pending'
    )
    return_date = models.DateTimeField(auto_now_add=True)  
    is_eligible = models.BooleanField(default=False)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    return_type = models.CharField(max_length=20, choices=[
        ('exchange', 'Exchange'),
        ('refund', 'Refund'),
        ('store_credit', 'Store Credit'),
    ], default='refund') 

    def __str__(self):
        return self.status

  
  