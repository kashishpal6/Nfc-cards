from django.urls import path
from .views import SignupView,VerifyOTPView,createProfile,listCompany,RetrieveCompany,DestroyCompany,createCompany,listProfile,RetrieveProfile,DestroyProfile,UpdateCompany,UpdateProfile
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('createProfile/',createProfile.as_view(),name="createProfile"),
    path('listProfile/',listProfile.as_view(),name="listprofile"),
    path('RetrieveProfile/<int:pk>/',RetrieveProfile.as_view(),name="RetrieveProfile"),
    path('UpdateProfile/<int:pk>/',UpdateProfile.as_view(),name="UpdateProfile"),
    path('DestroyProfile/<int:pk>/',DestroyProfile.as_view(),name="DestroyProfile"),
    path('createCompany/',createCompany.as_view(),name="createCompany"),
    path('listCompany/',listCompany.as_view(),name="listCompany"),
    path('RetrieveCompany/<int:pk>/',RetrieveCompany.as_view(),name="RetrieveCompany"),
    path('UpdateCompany/<int:pk>/',UpdateCompany.as_view(),name="UpdateCompany"),
    path('DestroyCompany/<int:pk>/',DestroyCompany.as_view(),name="DestroyCompany")
]

