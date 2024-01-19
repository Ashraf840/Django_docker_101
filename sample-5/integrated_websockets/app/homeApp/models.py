from django.db import models


class HomeModel(models.Model):
    image = models.ImageField(upload_to='image', default='image/default_image.png', blank=True)
