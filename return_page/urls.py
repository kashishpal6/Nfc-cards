from django.urls import path
from return_page.views import createReturnPage,listReturnPage,updateReturnPage,retrieveReturnPage


urlpatterns = [
   
    path('listReturnPage/',listReturnPage.as_view(),name="listReturnPage"),
    path('createReturnPage/',createReturnPage.as_view(),name="createReturnPage"),
    path('retrieveReturnPage/',retrieveReturnPage.as_view(),name="retrieveReturnPage"),
    path('updateReturnPage/',updateReturnPage.as_view(),name="updateReturnPage"),
]
