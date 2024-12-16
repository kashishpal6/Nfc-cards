from django.urls import path
from purchase.views import createPurchase,listpurchase,Retrievepurchase


urlpatterns = [
   
    path('createPurchase/',createPurchase.as_view(),name="create"),
    path('listPurchase/',listpurchase.as_view(),name="list"),
    path('Retrievepurchase/',Retrievepurchase.as_view(),name="Retrievepurchase")
 
]