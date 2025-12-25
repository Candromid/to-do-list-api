from django import forms
from .models import Task
from django.contrib.auth.models import User

class AdminTaskForm(forms.ModelForm):
    """
    Форма для админа.
    Админ может выбрать владельца задачи из всех пользователей.
    """
    owner = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'owner']
