from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    image = models.ImageField()
    desc = models.TextField()
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url