from django.db import models
from products.models import Products

class variant(models.Model):
    product = models.ForeignKey(Products, related_name='variants', on_delete=models.CASCADE)
    color = models.CharField(max_length=50, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    front_image = models.ImageField(upload_to='uploads/front_images/',null=True)
    back_image = models.ImageField(upload_to='uploads/back_images/',null=True)
    material_type = models.CharField(max_length=100,default="abc")
    shape = models.CharField(max_length=100,default = "rectangle")
    orientation = models.CharField(max_length=200,choices=[('horizontal','Horizontal'),('vertical','Vertical')],default='horizontal')

    
    def __str__(self):
        return f"{self.product.title} - {self.color}"

    class Meta:
        ordering = ['product', 'color']

