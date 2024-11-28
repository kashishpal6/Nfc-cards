from django.urls import path
from variant.views import createVariant,listVariant


urlpatterns = [
   
    path('create/',createVariant.as_view(),name="create"),
    path('list/',listVariant.as_view(),name="list"),
]
