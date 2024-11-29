from django.urls import path
from variant.views import createVariant,listVariant,RetrieveUpdateDestroyProducts


urlpatterns = [
   
    path('createVariant/',createVariant.as_view(),name="createVariant"),
    path('listVariant/',listVariant.as_view(),name="listVariant"),
    path('RetrieveUpdateDestroyProducts/',RetrieveUpdateDestroyProducts.as_view(),name="RetrieveUpdateDestroyProducts"),
]
