from django.urls import path
from products.views import createProducts,listProducts,RetrieveProducts,UpdateProducts,DestroyProducts


urlpatterns = [
   
    path('createProducts/',createProducts.as_view(),name="products"),
    path('listProducts/',listProducts.as_view(),name="listproducts"),
    path('RetrieveProducts/',RetrieveProducts.as_view(),name="RetrieveProducts"),
    path('UpdateProducts/',UpdateProducts.as_view(),name="UpdateProducts"),
    path('DestroyProducts/',DestroyProducts.as_view(),name="DestroyProducts"),
]

