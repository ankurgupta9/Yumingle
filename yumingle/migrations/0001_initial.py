# Generated by Django 5.0.2 on 2024-03-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_image', models.ImageField(upload_to='recipe_img')),
                ('recipe_name', models.CharField(max_length=20)),
                ('recipe_description', models.TextField()),
            ],
        ),
    ]
