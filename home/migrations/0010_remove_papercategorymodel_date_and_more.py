# Generated by Django 5.0.1 on 2024-01-21 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_paperdatemodel_alter_teamcategorymembermodel_header_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='papercategorymodel',
            name='date',
        ),
        migrations.AlterField(
            model_name='paperpdfmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_category', to='home.papercategorymodel'),
        ),
        migrations.DeleteModel(
            name='PaperDateModel',
        ),
    ]
