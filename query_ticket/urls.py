from django.urls import path
from query_ticket.views import createTicket,listTicket,RetrieveTicket,UpdateTicket,DestroyTicket


urlpatterns = [
   
    path('listTicket/',listTicket.as_view(),name="listTicket"),
    path('createTicket/',createTicket.as_view(),name="createTicket"),
    path('RetrieveTicket/<int:pk>/',RetrieveTicket.as_view(),name="RetrieveTicket"),
    path('UpdateTicket/<int:pk>/',UpdateTicket.as_view(),name="UpdateTicket"),
    path('DestroyTicket/<int:pk>/',DestroyTicket.as_view(),name="DestroyTicket"),
]

