# Generated by Django 3.0.6 on 2020-06-07 18:12

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contactform', '0008_auto_20200607_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='newsId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='txt',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=300, null=True),
        ),
    ]