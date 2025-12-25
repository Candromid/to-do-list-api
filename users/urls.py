from django.urls import path
from .views import register_view, RegisterView

urlpatterns = [
    # WEB
    path("register/", register_view, name="register"),

    # API
    path("api/register/", RegisterView.as_view(), name="api-register"),
]
