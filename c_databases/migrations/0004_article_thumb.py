# Generated by Django 5.0.3 on 2024-03-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_databases', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]