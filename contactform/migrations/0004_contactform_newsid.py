# Generated by Django 3.0.6 on 2020-06-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0003_contactform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='newsId',
            field=models.CharField(default='direct contact', max_length=999999),
        ),
    ]
