from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Task
from .serializers import TaskSerializer




class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)  # показываем только задачи текущего пользователя

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # привязываем задачу к текущему пользователю
        
        
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
