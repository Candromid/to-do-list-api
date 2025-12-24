from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

# DRF Router для API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
     path('tasks/page/', TaskListView.as_view(), name='task-list-page'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]

# Подключаем API маршруты
urlpatterns += router.urls
