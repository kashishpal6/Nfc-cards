from django.db import models
from contact_page.models import Contact

class Ticket(models.Model):
    Fullname = models.ForeignKey(Contact,on_delete=models.CASCADE,related_name='name',default='default')
    email =  models.ForeignKey(Contact,on_delete=models.CASCADE,related_name='contacts',default='email')
    query = models.ForeignKey(Contact,on_delete=models.CASCADE,related_name="queries")
    message = models.ForeignKey(Contact,on_delete=models.CASCADE,related_name="messages",default="message")
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
