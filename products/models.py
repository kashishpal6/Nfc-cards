from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    industry_type = models.CharField(max_length=100)
    service = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sellingPrice = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
      ordering =['title']
  
    def __str__(self):
      return self.title