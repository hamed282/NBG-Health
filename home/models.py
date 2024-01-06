from django.db import models


class HomeHeaderModel(models.Model):
    logo_header = models.ImageField(upload_to='images/header/')


class HomeFooterModel(models.Model):
    logo_footer = models.ImageField(upload_to='images/footer/')


class HomeContentModel(models.Model):
    title = models.CharField(max_length=255)
    h_title = models.CharField(max_length=255)
    h_image_left = models.ImageField(upload_to='images/content/')
    h_image_right = models.ImageField(upload_to='images/content/')
    title_ceo = models.CharField(max_length=255)
    name_ceo = models.CharField(max_length=255)
    ceo_image = models.ImageField(upload_to='images/content/')
    academic_title = models.CharField(max_length=255)
    study_field_title = models.CharField(max_length=255)
    description = models.CharField(max_length=2040)
    study_title = models.CharField(max_length=255)
    study_back_image = models.ImageField(upload_to='images/content/')
    study_forward_image = models.ImageField(upload_to='images/content/')
    study_video = models.FileField(upload_to='video/content/')







