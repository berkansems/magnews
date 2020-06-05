from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Main(models.Model):
    name=models.CharField(max_length=30)
    about=models.TextField(default="this site designed by berkan sems just for learning django ")
    facebook=models.CharField(default="https://www.facebook.com/behrang.shams",max_length=50)
    twitter=models.CharField(default="https://twitter.com/",max_length=50)
    instagram=models.CharField(default="https://www.instagram.com/behrang_shams/",max_length=50)

    def __str__(self):
        return self.name + "  ... id :" + str(self.pk)

class Suser(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)

