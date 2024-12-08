from django.urls import path
from products.views import createProducts,listProducts,RetrieveProducts,UpdateProducts,DestroyProducts


urlpatterns = [
   
    path('createProducts/',createProducts.as_view(),name="products"),
    path('listProducts/',listProducts.as_view(),name="listproducts"),
    path('RetrieveProducts/<int:pk>/',RetrieveProducts.as_view(),name="RetrieveProducts"),
    path('UpdateProducts/<int:pk>/',UpdateProducts.as_view(),name="UpdateProducts"),
    path('DestroyProducts/<int:pk>/',DestroyProducts.as_view(),name="DestroyProducts"),
]

