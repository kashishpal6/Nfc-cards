from django.urls import path
from .views import ReferSubscriptionCreateAPIView

urlpatterns = [
    path('create-referral/', ReferSubscriptionCreateAPIView.as_view(), name='create-referral'),
]
