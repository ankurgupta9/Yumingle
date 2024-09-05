# Generated by Django 5.0.2 on 2024-03-08 16:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yumingle', '0002_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_direction',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=50),
        ),
    ]
