# Generated by Django 4.2.7 on 2023-12-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_slug_alter_ingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
