from django.urls import path
from .views import RegisterView, AdminRegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('createadmin/', AdminRegisterView.as_view(), name="create_admin")
]