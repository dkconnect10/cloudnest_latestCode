from .views import RegisterUser,loginUser,GetProfile,UpdateProfile,logoutUser,ResetPassword,forgotPassword
from django.urls import path

urlpatterns = [
   path('RegisterUser/',RegisterUser.as_view(),name='RegisterUser'),
   path('loginUser/',loginUser.as_view(),name='loginUser'),
   path('GetProfile/',GetProfile.as_view(),name='GetProfile'),
   path('UpdateProfile/<int:pk>/',UpdateProfile.as_view(),name='UpdateProfile'),
   path('logoutUser/',logoutUser.as_view(),name='logoutUser'),
   path('ResetPassword/',ResetPassword.as_view(),name='ResetPassword'),
   path('forgotPassword/',forgotPassword.as_view(),name='forgotPassword')
]