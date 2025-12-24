from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # перечисляем все поля, кроме user, он будет добавляться автоматически
        fields = ['title', 'description', 'is_completed']
