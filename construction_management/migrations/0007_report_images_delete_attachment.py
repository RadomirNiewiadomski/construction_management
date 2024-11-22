# Generated by Django 5.1.3 on 2024-11-22 10:59

import construction_management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_management', '0006_remove_report_images_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=construction_management.models.report_image_file_path),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
