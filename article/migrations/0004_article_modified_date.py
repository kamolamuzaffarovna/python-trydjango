# Generated by Django 4.2.7 on 2023-11-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]