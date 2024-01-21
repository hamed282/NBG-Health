# Generated by Django 5.0.1 on 2024-01-21 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_morelandingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamCategoryMemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2040)),
                ('name', models.CharField(max_length=2040)),
                ('image', models.ImageField(upload_to='images/team_person/')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=2040)),
            ],
        ),
        migrations.DeleteModel(
            name='TeamPersonModel',
        ),
        migrations.AlterField(
            model_name='teamvaluescontentmodel',
            name='values_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_values', to='home.teamvaluesmodel'),
        ),
        migrations.AddField(
            model_name='teamcategorymembermodel',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_category', to='home.teamcategorymodel'),
        ),
    ]
