from django.urls import path
from products.views import createProducts,listProducts


urlpatterns = [
   
    path('contact-us/',createProducts.as_view(),name="contact"),
    path('list-contact_us/',listProducts.as_view(),name="list_contact_us"),
]
