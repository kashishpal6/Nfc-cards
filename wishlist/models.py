from django.db import models
from variant.models import variant
from auth_app.models import CustomUser

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="wishlist_items")
    variant_id= models.OneToOneField(variant,on_delete=models.CASCADE,related_name="wishlist_var")


    class Meta:
      ordering =['variant_id']
      unique_together = ('user','variant_id')   
  
    def __str__(self):
      return self.variant_id.product.title
