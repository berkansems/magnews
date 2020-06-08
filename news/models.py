from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import datetime
# Create your models here.
from django.utils import timezone
from ckeditor.fields import RichTextField


class News(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    short_text=models.CharField(max_length=150,null=True,blank=True)
    body_text= RichTextUploadingField(blank=True,null=True)
    date = models.CharField(max_length=12)
    pic= models.ImageField(null=True,blank=True)
    writer = models.CharField(max_length=50,null=True,blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    catId = models.IntegerField(null=True, blank=True)
    oCatId = models.IntegerField(null=True, blank=True)
    show = models.IntegerField(default=0,null=True, blank=True)
    rand = models.IntegerField(default=0)



    def __str__(self):
        return self.name + "  .  id :" + str(self.pk)