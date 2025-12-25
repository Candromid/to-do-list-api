from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Task
from .admin_forms import AdminTaskForm  # используем отдельную форму для админа

# Дашборд админа
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('task-list-page')

    users = User.objects.all()
    tasks = Task.objects.all().order_by('-updated_at')  # новые сверху

    # Фильтры
    user_filter = request.GET.get('user')
    status_filter = request.GET.get('status')
    if user_filter:
        tasks = tasks.filter(owner__id=user_filter)
    if status_filter == 'done':
        tasks = tasks.filter(is_completed=True)
    elif status_filter == 'pending':
        tasks = tasks.filter(is_completed=False)

    context = {
        'users': users,
        'tasks': tasks,
        'user_filter': user_filter,
        'status_filter': status_filter
    }
    return render(request, 'admin/dashboard.html', context)


# Добавление задачи
def admin_task_add(request):
    if not request.user.is_superuser:
        return redirect('task-list-page')

    if request.method == 'POST':
        form = AdminTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = AdminTaskForm()

    return render(request, 'admin/task_form.html', {'form': form, 'title': 'Добавить задачу'})


# Редактирование задачи
def admin_task_edit(request, pk):
    if not request.user.is_superuser:
        return redirect('task-list-page')

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = AdminTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = AdminTaskForm(instance=task)

    return render(request, 'admin/task_form.html', {'form': form, 'title': 'Редактировать задачу'})


# Удаление задачи
def admin_task_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('task-list-page')

    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('admin-dashboard')
