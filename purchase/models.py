from django.db import models
from auth_app.models import CustomUser
from variant.models import variant

class Purchase(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user")
    variant = models.ForeignKey(variant,on_delete=models.CASCADE,related_name="variants")
    

