from django.db import models
from auth_app.models import CustomUser
from variant.models import variant


class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="cart")
    variant=models.ForeignKey(variant,on_delete=models.CASCADE,related_name="var")
    front_data=models.JSONField()
    back_data=models.JSONField()


    class Meta:
      ordering =['variant']
  
    def __str__(self):
      return self.variant.product.title
