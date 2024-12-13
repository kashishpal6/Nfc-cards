from django.db import models
from contact_page.models import Contact

class Ticket(models.Model):
    fullname = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tickets_fullname', default=None)
    email = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tickets_email', default=None)
    query = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tickets_query', default=None)
    message = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tickets_message', default=None)
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
