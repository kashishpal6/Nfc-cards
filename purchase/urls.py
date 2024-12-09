from django.urls import path
from purchase.views import createPurchase,listpurchase


urlpatterns = [
   
    path('createPurchase/',createPurchase.as_view(),name="create"),
    path('listPurchase/',listpurchase.as_view(),name="list")
 
]