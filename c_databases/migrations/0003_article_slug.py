# Generated by Django 5.0.3 on 2024-03-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_databases', '0002_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]