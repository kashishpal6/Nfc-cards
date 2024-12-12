from django.db import models
from auth_app.models import CustomUser
from variant.models import variant

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="abc")
    variant = models.ForeignKey(variant,on_delete=models.CASCADE,related_name="xyz")
    quantity = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)


    class Meta:
      ordering =['variant']
  
    def __str__(self):
      return self.variant.product.title


