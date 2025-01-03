from django.db import models

class Banners(models.Model):
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to="banners/images/")

    class Meta:
      ordering =['type']
      verbose_name_plural = "banners"
  
    def __str__(self):
      return self.type