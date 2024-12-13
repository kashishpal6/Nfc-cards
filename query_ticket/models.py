from django.db import models
from contact_page.models import Contact

class Ticket(models.Model):
    Fullname = models.CharField(max_length=100)    
    email = models.EmailField()
    query = models.TextField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('resolve', 'Resolve'),
        ('assigned','Assigned'),
    ], default='pending')
    remarks = models.CharField(max_length=100)

    class Meta:
      ordering =['status']
  
    def __str__(self):
      return self.status
