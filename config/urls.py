from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# JWT (API авторизация)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Django-auth (WEB авторизация)
from django.contrib.auth.views import LoginView, LogoutView

# ===== Главная страница =====
def home(request):
    """
    Корень сайта /
    - если пользователь авторизован:
        - superuser → сразу в кастомную админку (/dashboard/)
        - обычный пользователь → личный кабинет (/tasks/page/)
    - если не авторизован → страница логина
    """
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            return redirect("admin-dashboard")
        else:
            return redirect("task-list-page")
    return redirect("login")


urlpatterns = [
    # ===== Корень сайта =====
    path("", home, name="home"),

    # ===== Стандартная админка Django =====
    path("admin/", admin.site.urls),

    # ===== JWT авторизация (API) =====
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ===== API пользователей =====
    path("api/users/", include("users.urls")),

    # ===== WEB: задачи и кастомная админка =====
    path("", include("tasks.urls")),

    # ===== WEB: аутентификация =====
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
    path("users/", include("users.urls")),  # явный префикс для регистрации/профиля
]
