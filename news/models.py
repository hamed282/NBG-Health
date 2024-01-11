from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    left_description = models.CharField(max_length=2040)
    right_description = models.CharField(max_length=2040)
    h_image_right = models.ImageField(upload_to='images/news/')
    slug = models.SlugField(max_length=20, unique=True)
