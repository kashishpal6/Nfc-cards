from django.db import models

# Create your models here.
class Services(models.Model):
    type=models.CharField(max_length=200,choices=[('nfc','NFC Card'),('menucard','Menu Card'),('vcard','Contact Card'),('payment','NFC with payment'),('miniweb','Web page')])
    description=models.TextField(max_length=500)
    price=models.PositiveIntegerField(default=999)
    image = models.ImageField(upload_to='images/')



    class Meta:
      ordering =['type']
  
    def __str__(self):
      return self.type