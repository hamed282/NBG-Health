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


class TeamPersonModel(models.Model):
    person_name = models.CharField(max_length=255)
    person_image = models.ImageField(upload_to='images/team_person/')
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)


class TeamContentModel(models.Model):
    mission_description = models.CharField(max_length=2040)
    vision_description = models.CharField(max_length=2040)


class TeamValuesModel(models.Model):
    values_title = models.CharField(max_length=2040)


class TeamValuesContentModel(models.Model):
    values_title = models.ForeignKey(TeamValuesModel, on_delete=models.CASCADE, related_name='team_values')
    values_description = models.CharField(max_length=2040)


class MoreLandingModel(models.Model):
    image = models.ImageField(upload_to='images/more_landing/')
    name = models.CharField(max_length=255)
    academic_title = models.CharField(max_length=255)
    executive_title = models.CharField(max_length=255)
    study_title = models.CharField(max_length=255)
    title = models.CharField(max_length=2040)
    description = models.CharField(max_length=8040)
