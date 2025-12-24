from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,TaskListView


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
]

urlpatterns += router.urls
