# Generated by Django 3.0.6 on 2020-06-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_news_rand'),
        ('contactform', '0009_auto_20200607_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='newsId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]
