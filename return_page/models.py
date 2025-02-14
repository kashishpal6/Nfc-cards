from django.db import models
from purchase.models import Purchase
from auth_app.models import CustomUser
class ReturnPage(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="pages")  
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name ="customer",default='00')
    productCode = models.CharField(max_length=100,default='default')
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
    quantity = models.IntegerField(default=00)  
    request_type = models.CharField(max_length=20, choices=[
        ('return', 'Return'),
        ('refund', 'Refund'),
        ('replacement', 'Replacement'),
    ], default='refund') 

    def __str__(self):
        return self.status

  
  