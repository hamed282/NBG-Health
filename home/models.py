from django.db import models


class HomeHeaderModel(models.Model):
    logo_header = models.ImageField(upload_to='images/header/')
    def __str__(self):
        return f'Home Header'


class HomeFooterModel(models.Model):
    logo_footer = models.ImageField(upload_to='images/footer/')
    def __str__(self):
        return f'Home Footer'


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

    def __str__(self):
        return f'Home content'

# class TeamPersonModel(models.Model):
#     person_name = models.CharField(max_length=255)
#     person_image = models.ImageField(upload_to='images/team_person/')
#     title = models.CharField(max_length=255)
#     header = models.CharField(max_length=255)


class TeamContentModel(models.Model):
    mission_description = models.CharField(max_length=2040)
    vision_description = models.CharField(max_length=2040)
    def __str__(self):
        return f'Team content'

class TeamValuesModel(models.Model):
    values_title = models.CharField(max_length=2040)
    def __str__(self):
        return f'{self.values_title}'


class TeamValuesContentModel(models.Model):
    values_title = models.ForeignKey(TeamValuesModel, on_delete=models.CASCADE, related_name='list_values')
    values_description = models.CharField(max_length=2040)

    def __str__(self):
        return self.values_description


class MoreLandingModel(models.Model):
    image = models.ImageField(upload_to='images/more_landing/')
    name = models.CharField(max_length=255)
    academic_title = models.CharField(max_length=255)
    executive_title = models.CharField(max_length=255)
    study_title = models.CharField(max_length=255)
    title = models.CharField(max_length=2040)
    description = models.CharField(max_length=8040)
    def __str__(self):
        return f'More Landing'

class TeamCategoryModel(models.Model):
    header = models.CharField(max_length=2040)
    priority = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.header}'
class TeamCategoryMemberModel(models.Model):
    header = models.ForeignKey(TeamCategoryModel, on_delete=models.CASCADE, related_name='team_category')
    title = models.CharField(max_length=2040)
    name = models.CharField(max_length=2040)
    image = models.ImageField(upload_to='images/team_person/')
    def __str__(self):
        return f'{self.header} - {self.title}'
class PaperDateModel(models.Model):
    date = models.CharField(max_length=255)
    def __str__(self):
        return self.date
class PaperCategoryModel(models.Model):
    date = models.ForeignKey(PaperDateModel, on_delete=models.CASCADE, related_name='date_paper')
    category = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.category} - {self.date}'
class PaperPdfModel(models.Model):
    category = models.ForeignKey(PaperCategoryModel, on_delete=models.CASCADE, related_name='paper_category')
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=f'pdf/')
    def __str__(self):
        return self.title

#{category.date}/{category.category}/