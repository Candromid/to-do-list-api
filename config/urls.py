from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('task-list-page')  # HTML список задач
    return redirect('login') # если не авторизован

urlpatterns = [
    path('', home),  # корень сайта → редирект
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('tasks.urls')),
    path('api/users/', include('users.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]