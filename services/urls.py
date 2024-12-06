from django.urls import path
from services.views import createServices,listServices,RetrieveServices,UpdateServices,DestroyServices


urlpatterns = [
   
    path('listServices/',listServices.as_view(),name="listServices"),
    path('createServices/',createServices.as_view(),name="createServices"),
    path('RetrieveServices/',RetrieveServices.as_view(),name="RetrieveServices"),
    path('UpdateServices/',UpdateServices.as_view(),name="UpdateServices"),
    path('DestroyServices/',DestroyServices.as_view(),name="DestroyServices"),
]

