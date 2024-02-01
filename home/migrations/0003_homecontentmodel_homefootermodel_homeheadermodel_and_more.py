# Generated by Django 5.0.1 on 2024-01-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_logoimagemodel_class_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('h_title', models.CharField(max_length=255)),
                ('h_image_left', models.ImageField(upload_to='images/content/')),
                ('h_image_right', models.ImageField(upload_to='images/content/')),
                ('title_ceo', models.CharField(max_length=255)),
                ('name_ceo', models.CharField(max_length=255)),
                ('ceo_image', models.ImageField(upload_to='images/content/')),
                ('academic_title', models.CharField(max_length=255)),
                ('study_field_title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2040)),
                ('study_title', models.CharField(max_length=255)),
                ('study_back_image', models.ImageField(upload_to='images/content/')),
                ('study_forward_image', models.ImageField(upload_to='images/content/')),
                ('study_video', models.FileField(upload_to='video/content/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeFooterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_header', models.ImageField(upload_to='images/footer/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeHeaderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_header', models.ImageField(upload_to='images/header/')),
            ],
        ),
        migrations.DeleteModel(
            name='LogoImageModel',
        ),
    ]
