# Generated by Django 5.0.1 on 2024-01-11 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_logo_header_homefootermodel_logo_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_description', models.CharField(max_length=2040)),
                ('vision_description', models.CharField(max_length=2040)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=255)),
                ('person_image', models.ImageField(upload_to='images/team_person/')),
                ('title', models.CharField(max_length=255)),
                ('header', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeamValuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values_title', models.CharField(max_length=2040)),
            ],
        ),
        migrations.CreateModel(
            name='TeamValuesContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values_description', models.CharField(max_length=2040)),
                ('values_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_values', to='home.teamvaluesmodel')),
            ],
        ),
    ]
