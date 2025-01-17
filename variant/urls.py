from django.urls import path
from variant.views import createVariant,listVariant,RetrieveVariant,UpdateVariant,DestroyVariant,ListVariantByProductID


urlpatterns = [
   
    path('createVariant/',createVariant.as_view(),name="createVariant"),
    path('listVariant/',listVariant.as_view(),name="listVariant"),
    path('RetrieveVariant/<int:pk>/',RetrieveVariant.as_view(),name="Retrievevariant"),
    path('ListVariantByProductID/<int:pk>/',ListVariantByProductID.as_view(),name = "ListVariantByProductID"),
    path('UpdateVariant/<int:pk>/',UpdateVariant.as_view(),name="Updatevariant"),
    path('DestroyVariant/<int:pk>/',DestroyVariant.as_view(),name="Destroyvariant"),
]



