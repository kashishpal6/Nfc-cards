from django.db import models

class Contact(models.Model):
    Fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10,default='0000')
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
      ordering =['Fullname']
  
    def __str__(self):
      return self.Fullname