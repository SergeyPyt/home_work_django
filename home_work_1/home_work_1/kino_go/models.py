from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=20, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["id"]

    def __str__(self):
        return f"{self.pk} - {self.genre}"


class Actor(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Имя")
    birth_date = models.DateField(verbose_name="Дата рождения")
    country = models.CharField(max_length=50, verbose_name="Страна")

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
        ordering = ["id"]

    def __str__(self):
        return f"{self.pk} - {self.full_name}"


class Film(models.Model):
    class Languages(models.TextChoices):
        RU = "Рус"
        GE = "Нем"
        UA = "Укр"
        PL = "Пол"

    title = models.CharField(max_length=150, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год")
    description = models.TextField(verbose_name="Описание")
    lang = models.CharField(max_length=15, choices=Languages.choices)

    actor = models.ManyToManyField(Actor)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["id"]

    def __str__(self):
        return f"{self.pk} - {self.title}"



