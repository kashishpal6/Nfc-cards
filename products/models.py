from django.db import models
from services.models import Services

class Products(models.Model):
    title = models.CharField(max_length=100)
    service = models.ForeignKey(Services,on_delete=models.CASCADE)
    description = models.TextField(blank=True)


    class Meta:
      ordering =['title']
      verbose_name_plural = "products"
  
    def __str__(self):
      return self.title