from django.db import models

# Create your models here.


class News(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    short_text=models.CharField(max_length=150,null=True,blank=True)
    body_text= models.CharField(max_length=1500,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pic= models.ImageField(null=True,blank=True)
    writer = models.CharField(max_length=50)



    def __str__(self):
        return self.name + "  ... id :" + str(self.pk)