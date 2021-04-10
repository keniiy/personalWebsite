from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField()
    location = models.CharField(max_length=150, blank=True)
    image = CloudinaryField('image')
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    youtube = models.CharField(max_length=150, blank=True)
    github = models.CharField(max_length=150, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)



    class Meta:
        verbose_name = ("Personal Info")
        verbose_name_plural = ("Personal Infos")

    def __str__(self):
        return self.name
