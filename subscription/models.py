from django.db import models
from auth_app.models import CustomUser

class referSubscription(models.Model):
    referred_by = models.ForeignKey(CustomUser,related_name='referred_by_subscriptions',on_delete=models.CASCADE)
    referred_to = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.referred_by}-{self.referred_to}"

  
    class Meta:
        unique_together = ('referred_by','referred_to')



  

# class SubscriptionPlan(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     duration = models.PositiveIntegerField(help_text="Duration in days")
#     created_at = models.DateTimeField(auto_now_add=True)
#     tenure = models.CharField(max_length=100)
#     discount = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class Subscription(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField()

#     def is_active(self):
#         return self.end_date >= datetime.now()

#     def __str__(self):
#         return f"{self.user.username} - {self.plan.name}"
    

# class refer(models.Model):
#     plan = models.ForeignKey(SubscriptionPlan,on_delete=models.CASCADE)
#     start_date = models.DateTimeField(auto_now_add =True)

    




    

    


