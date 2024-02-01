# Generated by Django 5.0.1 on 2024-01-31 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_teamcategorymodel_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperpdfmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_pdf', to='home.papercategorymodel'),
        ),
        migrations.AlterField(
            model_name='teamcategorymodel',
            name='priority',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='PaperPdfTitleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='pdf/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_category', to='home.papercategorymodel')),
            ],
        ),
    ]
