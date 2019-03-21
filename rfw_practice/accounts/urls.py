from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthView, RegisterAPIView
from accounts.user.views import UserDetailAPIView

urlpatterns = [
    path('', AuthView.as_view()),
    path('<str:username>/', UserDetailAPIView.as_view(), name = "detail"),
    path('<str:username>/status/', UserDetailAPIView.as_view(), name = "status_list"),
    path('register/', RegisterAPIView.as_view()),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token)
]
