from django.db import models

# Create your models here.

class Work(models.Model):

    image=models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=200)
    urltext=models.CharField(max_length=100,default="")
