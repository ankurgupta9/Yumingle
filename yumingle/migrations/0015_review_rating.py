# Generated by Django 5.0.2 on 2024-05-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yumingle', '0014_remove_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
