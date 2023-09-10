from django.db import models


class Marks(models.Model):
    marks = models.CharField(max_length=150, verbose_name="Отметки")

