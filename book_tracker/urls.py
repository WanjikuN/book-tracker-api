from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterView, ProfileView, LogoutView

urlpatterns = [
    # JWT token endpoints
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Custom auth endpoints
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]
