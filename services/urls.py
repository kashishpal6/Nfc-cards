from django.urls import path
from services.views import createServices,listServices,RetrieveServices,UpdateServices,DestroyServices


urlpatterns = [
   
    path('listServices/',listServices.as_view(),name="listServices"),
    path('createServices/',createServices.as_view(),name="createServices"),
    path('RetrieveServices/<int:pk>/',RetrieveServices.as_view(),name="RetrieveServices"),
    path('UpdateServices/<int:pk>/',UpdateServices.as_view(),name="UpdateServices"),
    path('DestroyServices/<int:pk>/',DestroyServices.as_view(),name="DestroyServices"),
]

