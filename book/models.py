from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf/')
    image=models.ImageField(upload_to='cover/image/',null=True,blank=True)

    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
        self.pdf.delete()
        self.image.delete()
        super().delete(*args,**kwargs)