from account.models import Account
from django.db.models.signals import pre_save
from django.db import models
from .utils import unique_slug_generator


class Announcement(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    city = models.CharField(max_length=128, blank=False)
    details = models.CharField(max_length=128, blank=True, null=True)
    voivodeship = models.CharField(max_length=128, blank=False)

# https://www.youtube.com/watch?v=d5LYM3C_A98


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Announcement)
