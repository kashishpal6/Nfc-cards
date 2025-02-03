from django.urls import path
from .views import VerifyOTPView,SignupOrLoginView,listUser,createProfile,listCompany,RetrieveCompany,DestroyCompany,createCompany,listProfile,RetrieveProfile,DestroyProfile,UpdateCompany,UpdateProfile,UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('login/',SignupOrLoginView.as_view(),name = 'login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('listUser/',listUser.as_view(),name = "listUser"),
    path('createProfile/',createProfile.as_view(),name="createProfile"),
    path('listProfile/',listProfile.as_view(),name="listprofile"),
    path('RetrieveProfile/',RetrieveProfile.as_view(),name="RetrieveProfile"),
    path('UpdateProfile/',UpdateProfile.as_view(),name="UpdateProfile"),
    path('DestroyProfile/',DestroyProfile.as_view(),name="DestroyProfile"),
    path('createCompany/',createCompany.as_view(),name="createCompany"),
    path('listCompany/',listCompany.as_view(),name="listCompany"),
    path('RetrieveCompany/',RetrieveCompany.as_view(),name="RetrieveCompany"),
    path('UpdateCompany/',UpdateCompany.as_view(),name="UpdateCompany"),
    path('DestroyCompany/',DestroyCompany.as_view(),name="DestroyCompany"),
    path('UserProfileView/<uuid:pk>/',UserProfileView.as_view(),name="UserProfileView")
]

