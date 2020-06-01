# Generated by Django 3.0.6 on 2020-05-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200524_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(blank=True, choices=[('sport', 'sport'), ('game', 'game'), ('politics', 'politics'), ('cultural', 'cultural')], max_length=30, null=True),
        ),
    ]