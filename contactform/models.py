from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    txt=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    website=models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):
        return self.name