from django.db import models
from django.contrib.auth.models import User
from ..category.models import Category

# Create your models here.
class PostType(models.Model):
    title = models.CharField(default="Offres", max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField (max_length=100)
    an_type = models.ForeignKey(PostType, default=None, on_delete=models.PROTECT)
    price = models.CharField (max_length=100)
    content = models.TextField (max_length=1000)
    num_street = models.CharField (max_length=40)
    street = models.CharField (max_length=40)
    city = models.CharField (max_length=40)
    postalcode = models.CharField (max_length=10)
    country = models.CharField (max_length=40)
    #thumb = models.TextField (max_length=1000, default=None)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, default=None, on_delete=models.PROTECT)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title