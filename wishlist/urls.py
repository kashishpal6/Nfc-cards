from django.urls import path
from wishlist.views import createWishlist,listWishlist,RetrieveWishlist,DestroyWishlist,UpdateWishlist


urlpatterns = [
   
    path('createWishlist/',createWishlist.as_view(),name="create"),
    path('listWishlist/',listWishlist.as_view(),name="list"),
    path('RetrieveWishlist/<int:pk>/',RetrieveWishlist.as_view(),name="Retrieve"),
    path('UpdateWishlist/<int:pk>/',UpdateWishlist.as_view(),name="Update"),
    path('DestroyWishlist/<int:pk>/',DestroyWishlist.as_view(),name="Destroy")
]