from django.db import models


class GalleryImageSlideModel(models.Model):
    title = models.CharField(max_length=255)
    image_slide = models.ImageField(upload_to='images/gallery/slide')


class GalleryVideoSlideModel(models.Model):
    title = models.CharField(max_length=255)
    video_slide = models.FileField(upload_to='video/gallery/slide')


class GalleryContentModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/gallery/image')
