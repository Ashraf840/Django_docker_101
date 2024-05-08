from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profilePicture', default='profilePicture/default_avatar.png', blank=True)
