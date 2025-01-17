from django.db import models
from auth_app.models import CustomUser
from variant.models import variant
from AddToCart.models import Cart

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="abc")
    variant = models.ForeignKey(variant,on_delete=models.CASCADE,related_name="xyz")
    quantity = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart")


    class Meta:
      ordering =['variant']
  
    def __str__(self):
      return str(self.id)


