# Generated by Django 4.2.5 on 2023-09-07 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kino_go', '0006_change_model_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kino_go.genre'),
        ),
    ]
