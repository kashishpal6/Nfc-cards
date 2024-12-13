from django.db import models
from contact_page.models import Contact

class Ticket(models.Model):
    query = models.ForeignKey(Contact,on_delete=models.CASCADE,related_name="ticket")
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('resolve', 'Resolve'),
    ], default='pending')
    remarks = models.CharField(max_length=100)

    class Meta:
      ordering =['status']
  
    def __str__(self):
      return self.status
