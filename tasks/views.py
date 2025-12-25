from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task
from .serializers import TaskSerializer



class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    # IsOwner = owner или админ (как мы обсуждали)

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()        # админ видит всё

        return Task.objects.filter(owner=user)  # пользователь — только свои

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # назначаем владельца



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        # показываем только задачи текущего пользователя
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()        # админ

        return Task.objects.filter(owner=user)  # пользователь


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list-page')  # HTML список задач

    def form_valid(self, form):
        # ⚡️ Привязываем задачу к текущему пользователю
        form.instance.owner = self.request.user  # владелец задачи 
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task-list-page')
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()        # админ может редактировать всё

        return Task.objects.filter(owner=user)  # пользователь — только свои

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list-page')
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Task.objects.all()        # админ удаляет всё

        return Task.objects.filter(owner=user)  # пользователь — только свои
