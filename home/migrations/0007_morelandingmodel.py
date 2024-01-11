# Generated by Django 5.0.1 on 2024-01-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_team_description_teamcontentmodel_mission_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreLandingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/more_landing/')),
                ('name', models.CharField(max_length=255)),
                ('academic_title', models.CharField(max_length=255)),
                ('executive_title', models.CharField(max_length=255)),
                ('study_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=2040)),
                ('description', models.CharField(max_length=8040)),
            ],
        ),
    ]
