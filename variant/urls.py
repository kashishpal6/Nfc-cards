from django.urls import path
from variant.views import createVariant,listVariant,RetrieveUpdateDestroyVariant


urlpatterns = [
   
    path('createVariant/',createVariant.as_view(),name="createVariant"),
    path('listVariant/',listVariant.as_view(),name="listVariant"),
    path('RetrieveUpdateDestroyVariant/<int:pk>/',RetrieveUpdateDestroyVariant.as_view(),name="RetrieveUpdateDestroyvariant"),
]
