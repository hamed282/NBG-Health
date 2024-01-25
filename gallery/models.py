from django.db import models


class GalleryImageSlideModel(models.Model):
    title = models.CharField(max_length=255)
    image_slide = models.ImageField(upload_to='images/gallery/slide')
    def __str__(self):
        return self.title


class GalleryVideoSlideModel(models.Model):
    title = models.CharField(max_length=255)
    video_slide = models.FileField(upload_to='video/gallery/slide')
    def __str__(self):
        return self.title

class GalleryContentModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/gallery/image')
    def __str__(self):
        return self.title
