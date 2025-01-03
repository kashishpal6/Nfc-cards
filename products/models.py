from django.db import models
from services.models import Services

class Products(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/images/',null=True)
    service = models.ForeignKey(Services,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    IsPremium = models.BooleanField(default=False)

    class Meta:
      ordering =['title']
      verbose_name_plural = "products"
  
    def __str__(self):
      return self.title