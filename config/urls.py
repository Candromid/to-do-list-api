from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# JWT (API авторизация)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Django-auth (WEB авторизация)
from django.contrib.auth.views import LoginView, LogoutView

# ===== Главная страница =====
def home(request):
    """
    Корень сайта /
    - если пользователь авторизован → личный кабинет (HTML)
    - если нет → страница логина
    """
    if request.user.is_authenticated:
        return redirect("task-list-page")
    return redirect("login")


urlpatterns = [
    # ===== Корень сайта =====
    path("", home, name="home"),

    # ===== Админка Django =====
    # Доступна только superuser / staff
    path("admin/", admin.site.urls),

    # ===== JWT авторизация (API) =====
    # Используется для REST / Postman / Frontend / Mobile
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ===== API пользователей и регистрация =====
    # /api/users/register/
    path("api/users/", include("users.urls")),

    # ===== WEB: задачи и личный кабинет =====
    # HTML страницы
    path("", include("tasks.urls")),

    # ===== WEB: аутентификация =====
    # /login/
    # /logout/
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout",
    ),

    # ===== WEB: регистрация =====
    # /register/
    path("", include("users.urls")),
]