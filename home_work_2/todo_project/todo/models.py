from django.db import models


class TodoListItem(models.Model):
    content = models.CharField(max_length=100, verbose_name="Задача")

    class Meta:
        ordering = ['id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.id} - {self.content}"

    def __repr__(self):
        return f"{self.id} - {self.content}"
