from django.urls import path
from payment.views import createPayment,listPayment,retrievePayment,updatePayment,destroyPayment


urlpatterns = [
   
    path('createPayment/',createPayment.as_view(),name="createPayment"),
    path('listPayment/',listPayment.as_view(),name="listPayment"),
    path('retrievePayment/<int:pk>/',retrievePayment.as_view(),name="retrievePayment"),
    path('updatePayment/<int:pk>/',updatePayment.as_view(),name="updatePayment"),
    path('destroyPayment/<int:pk>/',destroyPayment.as_view(),name="destroyPayment"),
]
