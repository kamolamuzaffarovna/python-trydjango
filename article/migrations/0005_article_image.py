# Generated by Django 4.2.7 on 2023-11-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]