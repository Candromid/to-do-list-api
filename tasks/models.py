from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(          # владелец задачи
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    title = models.CharField(max_length=255)   # название
    description = models.TextField(blank=True) # описание
    is_completed = models.BooleanField(default=False)  # статус

    created_at = models.DateTimeField(auto_now_add=True)  # создано
    updated_at = models.DateTimeField(auto_now=True)      # обновлено

    class Meta:
        ordering = ['-created_at']      # новые сверху

    def __str__(self):
        return f'{self.title} ({self.owner.username})'
