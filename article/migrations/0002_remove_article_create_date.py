# Generated by Django 4.2.7 on 2023-11-27 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='create_date',
        ),
    ]
