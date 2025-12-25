from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)
from .admin_views import (
    admin_dashboard,
    admin_task_add,
    admin_task_edit,
    admin_task_delete
)

# DRF Router для API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # WEB-интерфейс для обычного пользователя
    path('tasks/page/', TaskListView.as_view(), name='task-list-page'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # Кастомная админка (без конфликта со стандартной /admin/)
    path('dashboard/', admin_dashboard, name='admin-dashboard'),
    path('dashboard/task/add/', admin_task_add, name='admin-task-add'),
    path('dashboard/task/<int:pk>/edit/', admin_task_edit, name='admin-task-edit'),
    path('dashboard/task/<int:pk>/delete/', admin_task_delete, name='admin-task-delete'),
]

# Подключаем маршруты DRF API
urlpatterns += router.urls
