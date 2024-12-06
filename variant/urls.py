from django.urls import path
from variant.views import createVariant,listVariant,RetrieveVariant,UpdateVariant,DestroyVariant


urlpatterns = [
   
    path('createVariant/',createVariant.as_view(),name="createVariant"),
    path('listVariant/',listVariant.as_view(),name="listVariant"),
    path('RetrieveVariant/',RetrieveVariant.as_view(),name="Retrievevariant"),
    path('UpdateVariant/',UpdateVariant.as_view(),name="Updatevariant"),
    path('DestroyVariant/',DestroyVariant.as_view(),name="Destroyvariant"),
]



