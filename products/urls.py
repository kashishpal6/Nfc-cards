from django.urls import path
from products.views import createProducts,listProducts,RetrieveUpdateDestroyProducts


urlpatterns = [
   
    path('createProducts/',createProducts.as_view(),name="products"),
    path('listProducts/',listProducts.as_view(),name="listproducts"),
    path('RetrieveUpdateDestroyProducts/<int:pk>/',RetrieveUpdateDestroyProducts.as_view(),name="RetrieveUpdateDestroyProducts"),
]
