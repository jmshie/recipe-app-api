# Generated by Django 3.2.25 on 2024-05-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_recipe"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="link",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
