# Generated by Django 4.2.5 on 2023-09-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino_go', '0003_add_model_actor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['id'], 'verbose_name': 'Актер', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['id'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['id'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(max_length=10, verbose_name='Год'),
        ),
    ]