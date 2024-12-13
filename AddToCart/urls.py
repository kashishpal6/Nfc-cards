from django.urls import path
from AddToCart.views import createCart,listCart,RetrieveCart,UpdateCart,DestroyCart


urlpatterns = [
   
    path('createCart/',createCart.as_view(),name="create"),
    path('listCart/',listCart.as_view(),name="list"),
    path('RetrieveCart/',RetrieveCart.as_view(),name="Retrieve"),
    path('UpdateCart',UpdateCart.as_view(),name="Update"),
    path('DestroyCart',DestroyCart.as_view(),name="Destroy")
]