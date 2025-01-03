from django.urls import path
from .views import CreateBanner,UpdateBanner,DestroyBanner

urlpatterns = [
    path('CreateBanner/', CreateBanner.as_view(), name='create-banner'),
    path('UpdateBanner/<int:pk>/',UpdateBanner.as_view(),name="UpdateBanner"),
    path('DestroyBanner/<int:pk>/',DestroyBanner.as_view(),name="DestroyBanner"),
]
