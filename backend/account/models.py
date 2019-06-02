from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.PROTECT)
    status = (
        ('1', 'Etudiant'),
        ('2', 'Professeur'),
    )
    num_street = models.CharField(max_length=4)
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
