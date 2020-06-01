from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import datetime
# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField


class SubCategory(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    catName=models.CharField(max_length=30,null=True,blank=True)
    catId=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.name