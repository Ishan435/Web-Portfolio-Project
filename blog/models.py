from django.db import models

# Create your models here.


class Blog(models.Model):

    title=models.CharField(max_length=255)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="images/")
    text = models.TextField()

    def summary(self):
        return self.text[:100]

    def __str__(self):
        return self.title    
