from django.contrib import admin
from django.urls import path, include

from .views import UserDetailAPIView, UserStatusAPIView

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name = "detail"),
    path('<str:username>/status/', UserStatusAPIView.as_view(), name = "status_list"),
]
