from django.db import models
import datetime
# Create your models here.
from django.utils import timezone


class Cat(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):
        return self.name + "  .  id :" + str(self.pk)


from django.db import models

# Create your models here.
