from django.db import models


class Lesson0(models.Model):
    lesson = models.CharField(max_length=100, verbose_name="Занятие" )

