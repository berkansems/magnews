from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from news.models import News


class ContactForm(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    txt=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    website=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    txt=RichTextUploadingField(max_length=300,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    website=models.CharField(max_length=30,null=True,blank=True)
    newsId=models.ForeignKey(News,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name