# Generated by Django 5.0.1 on 2024-01-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_paperdatemodel_papercategorymodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcategorymodel',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
