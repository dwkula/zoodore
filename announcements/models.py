from account.models import Account
from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Announcement(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    slug = models.SlugField(max_length=50, null=True)
    phone = PhoneNumberField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    city = models.CharField(max_length=128, blank=False)
    details = models.CharField(max_length=128, blank=True, null=True)
    voivodeship = models.CharField(max_length=128, blank=False)

# https://www.youtube.com/watch?v=d5LYM3C_A98
