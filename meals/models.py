from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


class Meals(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='media/', default=True)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name
