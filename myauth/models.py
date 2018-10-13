from django.db import models

# Create your models here.
class General_Secretary(models.Model):
    photo = models.ImageField()
    designation = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description =models.TextField()

    def __str__(self):
        return self.designation