from django.db import models

# Create your models here.
class Services(models.Model):
    type=models.CharField(max_length=200,choices=[('nfc','NFC Card'),('menucard','Menu Card'),('vcard','Contact Card'),('payment','NFC with payment'),('miniweb','Web page')])
    description=models.TextField(max_length=500)
    price=models.PositiveIntegerField(default=999)
    image = models.ImageField(upload_to='services/')



    class Meta:
      ordering =['type']
      verbose_name_plural = "services"
  
    def __str__(self):
      return self.type