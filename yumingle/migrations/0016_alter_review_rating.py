# Generated by Django 5.0.2 on 2024-05-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yumingle', '0015_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
